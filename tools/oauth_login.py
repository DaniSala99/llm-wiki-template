#!/usr/bin/env python3
"""
Interactive Google OAuth2 login for LLM Wiki.
Saves credentials for future use without browser interaction.
"""

import os
import json
import webbrowser
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import base64
import requests

CREDS_DIR = Path.home() / ".config" / "llm-wiki"
CREDS_FILE = CREDS_DIR / "oauth_creds.json"

# Simulated OAuth flow (you'll need to replace with real client_id/secret)
# For now, we'll create a helper to get credentials from Google
SCOPES = "https://www.googleapis.com/auth/drive"

class OAuthHandler(BaseHTTPRequestHandler):
    auth_code = None

    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)

        if 'code' in params:
            self.auth_code = params['code'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>✓ Autenticazione riuscita!</h1><p>Puoi chiudere questa finestra.</p>")
            print("\n✓ Authorization code received!")
        elif 'error' in params:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"<h1>✗ Errore: {params['error'][0]}</h1>".encode())

    def log_message(self, format, *args):
        pass  # Suppress log messages

def authenticate_with_browser():
    """
    Start OAuth flow in browser.
    Note: This requires CLIENT_ID and CLIENT_SECRET from Google Cloud Console
    """
    print("=" * 60)
    print("AUTENTICAZIONE GOOGLE OAUTH2")
    print("=" * 60)

    # Check if credentials already exist
    if CREDS_FILE.exists():
        with open(CREDS_FILE) as f:
            creds = json.load(f)
            print(f"\n✓ Credenziali trovate: {creds.get('client_id')[:20]}...")
            return creds

    print("\n⚠️  Per autenticarti con Google Drive, hai bisogno di:")
    print("   1. Un progetto in Google Cloud Console")
    print("   2. OAuth 2.0 Desktop Client ID e Secret")
    print("\nPassi:")
    print("   1. Vai a: https://console.cloud.google.com")
    print("   2. Crea un nuovo progetto o selezionane uno")
    print("   3. Abilita 'Google Drive API'")
    print("   4. Crea credenziali OAuth2 (Desktop Application)")
    print("   5. Scarica il JSON e salvalo come 'client_secret.json'")
    print("   6. Copia il contenuto qui sotto quando richiesto")
    print("\nAlternativa veloce:")
    print("   Usa questo script pre-configurato (richiede registrazione):")
    print("   https://github.com/gsuitedevs/python-quickstart")

    return None

def setup_with_manual_token():
    """
    Alternative: User provides refresh_token directly
    """
    print("\n" + "=" * 60)
    print("SETUP MANUALE - Incolla il tuo Refresh Token")
    print("=" * 60)

    print("\nSe hai già un refresh_token di Google:")
    refresh_token = input("\nIncolla il refresh_token (o premi Invio per saltare): ").strip()

    if refresh_token:
        # Minimal creds with refresh token
        creds = {
            "type": "authorized_user",
            "client_id": "default",
            "client_secret": "default",
            "refresh_token": refresh_token
        }

        CREDS_DIR.mkdir(parents=True, exist_ok=True)
        with open(CREDS_FILE, 'w') as f:
            json.dump(creds, f)

        print(f"\n✓ Credenziali salvate in {CREDS_FILE}")
        print(f"\nUsa: export GOOGLE_USER_CREDENTIALS='{json.dumps(creds)}'")
        return creds

    return None

if __name__ == "__main__":
    creds = authenticate_with_browser()

    if not creds:
        creds = setup_with_manual_token()

    if creds:
        print("\n✓ OAuth configurato!")
        print(f"\nPer usarlo, esegui:")
        print(f"export GOOGLE_USER_CREDENTIALS='{json.dumps(creds)}'")
        print(f"cd /tmp/wiki-project")
        print(f"python3 ../../workspaces/llm-wiki-template/tools/sync_project.py push CFMR-Lombardia")
    else:
        print("\n✗ Autenticazione non completata")
