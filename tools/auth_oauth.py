#!/usr/bin/env python3
"""
Google OAuth2 authentication for LLM Wiki projects.
Run this once to generate credentials, then use them for sync_project.py
"""

import json
import os
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ["https://www.googleapis.com/auth/drive"]
CREDS_FILE = Path.home() / ".config" / "llm-wiki-oauth.json"


def authenticate():
    """Authenticate and save credentials."""
    # Create a flow object
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secrets.json",  # Need to download from Google Cloud Console
        scopes=SCOPES,
        redirect_uri="http://localhost:8080"
    )

    # Run the flow
    creds = flow.run_local_server(port=8080)

    # Save credentials
    creds_dict = {
        "type": "authorized_user",
        "client_id": creds.client_id,
        "client_secret": creds.client_secret,
        "refresh_token": creds.refresh_token,
    }

    CREDS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CREDS_FILE, "w") as f:
        json.dump(creds_dict, f)

    print(f"✓ Credentials saved to {CREDS_FILE}")
    print(f"\nNow set environment variable:")
    print(f"export GOOGLE_USER_CREDENTIALS='{json.dumps(creds_dict)}'")

    return creds_dict


if __name__ == "__main__":
    try:
        creds = authenticate()
        print(f"\n✓ Authentication successful!")
    except FileNotFoundError:
        print("✗ Error: client_secrets.json not found")
        print("\nTo set up OAuth:")
        print("1. Go to https://console.cloud.google.com")
        print("2. Create OAuth 2.0 Desktop Application credentials")
        print("3. Download as JSON and save as client_secrets.json")
        print("4. Run this script again")
