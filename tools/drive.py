#!/usr/bin/env python3
"""
Google Drive API wrapper for LLM Wiki projects.
Handles file upload/download and folder management.
"""

import os
import json
import base64
from pathlib import Path
from typing import Optional

from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
import io


class DriveClient:
    """Google Drive API client."""

    def __init__(self, credentials_json: str):
        """Initialize with service account JSON string."""
        creds_dict = json.loads(credentials_json)
        self.creds = Credentials.from_service_account_info(
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


def load_credentials() -> Optional[str]:
    """Load Google service account credentials from environment."""
    creds_json = os.getenv("GOOGLE_SERVICE_ACCOUNT")
    if not creds_json:
        print("✗ GOOGLE_SERVICE_ACCOUNT environment variable not set")
        return None
    return creds_json


def get_client() -> Optional[DriveClient]:
    """Get authenticated Drive client."""
    creds_json = load_credentials()
    if not creds_json:
        return None

    try:
        return DriveClient(creds_json)
    except Exception as e:
        print(f"✗ Failed to initialize Drive client: {e}")
        return None
