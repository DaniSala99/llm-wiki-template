#!/bin/bash
# Helper script to authenticate with Google Drive using OAuth2

echo "🔐 Google Drive OAuth2 Authentication Helper"
echo ""
echo "This script will help you authenticate with your personal Google account"
echo "for wiki push/pull operations."
echo ""

# Option 1: Use Claude MCP
echo "Option 1: Use Claude's built-in Google Drive MCP"
echo "───────────────────────────────────────────────"
echo "Run this in Claude Code:"
echo "  /mcp"
echo ""
echo "Then select 'claude.ai Google Drive' to authenticate."
echo "The MCP server will handle all authentication automatically."
echo ""
echo "Once authenticated, the wiki commands will work:"
echo "  ./tools/wiki.sh CFMR-Lombardia"
echo ""
echo "───────────────────────────────────────────────"
echo ""

# Option 2: Manual OAuth2
echo "Option 2: Manual OAuth2 setup (for reference)"
echo "───────────────────────────────────────────────"
echo "If you want to use environment variables instead:"
echo ""
echo "1. Go to: https://myaccount.google.com/permissions"
echo "2. Scroll to 'Third-party apps with account access'"
echo "3. Look for 'Claude Code' or similar OAuth apps"
echo ""
echo "Or authenticate via:"
echo "  gcloud auth application-default login"
echo ""
echo "Then the code will use: GOOGLE_USER_CREDENTIALS"
echo ""

# Option 3: Check current auth status
echo ""
echo "Current authentication status:"
echo "───────────────────────────────────────────────"

if [ -n "$GOOGLE_SERVICE_ACCOUNT" ]; then
    echo "✓ GOOGLE_SERVICE_ACCOUNT is set (service account mode)"
    echo "  ⚠ Service accounts cannot push to personal Drive"
    echo "  → Use Option 1 (Claude MCP) instead"
fi

if [ -n "$GOOGLE_USER_CREDENTIALS" ]; then
    echo "✓ GOOGLE_USER_CREDENTIALS is set (user OAuth mode)"
    echo "  → Ready to use ./tools/wiki.sh CFMR-Lombardia"
fi

if [ -z "$GOOGLE_SERVICE_ACCOUNT" ] && [ -z "$GOOGLE_USER_CREDENTIALS" ]; then
    echo "⚠ No credentials are currently set"
    echo "  → Use Option 1 (Claude MCP) to authenticate"
fi

echo ""
echo "───────────────────────────────────────────────"
echo ""
echo "Need help? Check:"
echo "  - Google Drive scope: https://www.googleapis.com/auth/drive"
echo "  - Claude MCP docs: https://github.com/anthropics/claude-code"
