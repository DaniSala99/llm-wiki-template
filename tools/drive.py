#!/usr/bin/env python3
"""
Google Drive API wrapper for LLM Wiki projects.
Handles file upload/download and folder management.
Supports both service account and OAuth2 user credentials.
"""

import os
import json
import base64
from pathlib import Path
from typing import Optional

from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from google.oauth2.credentials import Credentials as UserCredentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
import io


class DriveClient:
    """Google Drive API client."""

    def __init__(self, credentials_json: str = None, is_service_account: bool = True):
        """Initialize with service account or user OAuth credentials.

        Args:
            credentials_json: JSON string of credentials
            is_service_account: If True, treat as service account. If False, user OAuth.
        """
        if not credentials_json:
            raise ValueError("credentials_json is required")

        creds_dict = json.loads(credentials_json)

        if is_service_account:
            self.creds = ServiceAccountCredentials.from_service_account_info(
                creds_dict,
                scopes=["https://www.googleapis.com/auth/drive"]
            )
        else:
            # User OAuth credentials
            self.creds = UserCredentials.from_authorized_user_info(
                creds_dict,
                scopes=["https://www.googleapis.com/auth/drive"]
            )

        self.service = build("drive", "v3", credentials=self.creds)

    def list_files(self, folder_id: str, name_pattern: Optional[str] = None) -> list:
        """List all files in a folder."""
        query = f"'{folder_id}' in parents and trashed=false"
        if name_pattern:
            query += f" and name contains '{name_pattern}'"

        results = self.service.files().list(
            q=query,
            spaces="drive",
            fields="files(id, name, mimeType, modifiedTime)",
            pageSize=1000
        ).execute()

        return results.get("files", [])

    def download_file(self, file_id: str, local_path: Path) -> bool:
        """Download a file from Drive."""
        try:
            request = self.service.files().get_media(fileId=file_id)
            fh = io.FileIO(local_path, "wb")
            downloader = MediaIoBaseDownload(fh, request)

            done = False
            while not done:
                status, done = downloader.next_chunk()

            fh.close()
            return True
        except Exception as e:
            print(f"✗ Download error for {file_id}: {e}")
            return False

    def upload_file(self, local_path: Path, folder_id: str, filename: Optional[str] = None) -> Optional[str]:
        """Upload or update a file in Drive."""
        try:
            filename = filename or local_path.name

            # Check if file exists
            existing = self.service.files().list(
                q=f"'{folder_id}' in parents and name='{filename}' and trashed=false",
                spaces="drive",
                fields="files(id)",
                pageSize=1
            ).execute()

            file_metadata = {"name": filename}
            media = MediaFileUpload(local_path, resumable=True)

            if existing.get("files"):
                # Update existing file
                file_id = existing["files"][0]["id"]
                self.service.files().update(
                    fileId=file_id,
                    media_body=media,
                    fields="id"
                ).execute()
            else:
                # Create new file
                file_metadata["parents"] = [folder_id]
                self.service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields="id"
                ).execute()

            return True
        except Exception as e:
            print(f"✗ Upload error for {local_path}: {e}")
            return False

    def get_or_create_folder(self, name: str, parent_id: str) -> str:
        """Get folder ID or create if doesn't exist."""
        # Check if folder exists
        existing = self.service.files().list(
            q=f"'{parent_id}' in parents and name='{name}' and mimeType='application/vnd.google-apps.folder' and trashed=false",
            spaces="drive",
            fields="files(id)",
            pageSize=1
        ).execute()

        if existing.get("files"):
            return existing["files"][0]["id"]

        # Create new folder
        file_metadata = {
            "name": name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_id]
        }
        folder = self.service.files().create(
            body=file_metadata,
            fields="id"
        ).execute()

        return folder.get("id")

    def delete_file(self, file_id: str) -> bool:
        """Delete a file from Drive."""
        try:
            self.service.files().delete(fileId=file_id).execute()
            return True
        except Exception as e:
            print(f"✗ Delete error for {file_id}: {e}")
            return False


def load_credentials() -> tuple[Optional[str], bool]:
    """Load Google credentials from environment.

    Returns:
        (credentials_json, is_service_account) tuple
        Tries GOOGLE_SERVICE_ACCOUNT first, falls back to GOOGLE_USER_CREDENTIALS
    """
    # Try service account first
    service_account_json = os.getenv("GOOGLE_SERVICE_ACCOUNT")
    if service_account_json:
        return (service_account_json, True)

    # Fall back to user OAuth credentials
    user_creds_json = os.getenv("GOOGLE_USER_CREDENTIALS")
    if user_creds_json:
        return (user_creds_json, False)

    # Try to use the MCP Server for Google Drive authentication
    try:
        import subprocess
        result = subprocess.run(
            ["claude", "--model", "haiku", "--no-vision"],
            input="Get Google Drive credentials using the MCP server",
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print("ℹ Using Claude MCP Google Drive authentication")
            return ("mcp", False)  # Special marker for MCP auth
    except Exception:
        pass

    print("✗ No Google credentials found.")
    print("  Set either GOOGLE_SERVICE_ACCOUNT or GOOGLE_USER_CREDENTIALS environment variable")
    print("  Or use: claude /mcp to authenticate with Google Drive")
    return (None, False)


def get_client() -> Optional[DriveClient]:
    """Get authenticated Drive client."""
    creds_json, is_service_account = load_credentials()
    if not creds_json:
        return None

    try:
        return DriveClient(creds_json, is_service_account=is_service_account)
    except Exception as e:
        print(f"✗ Failed to initialize Drive client: {e}")
        return None
