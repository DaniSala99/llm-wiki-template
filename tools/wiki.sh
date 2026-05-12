#!/bin/bash
set -e

# Wiki automation script - orchestrates full ingestion workflow
# Usage: ./tools/wiki.sh <project-name>

if [ $# -ne 1 ]; then
    echo "Usage: $0 <project-name>"
    echo "Example: $0 CFMR-Lombardia"
    exit 1
fi

PROJECT_NAME="$1"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT_DIR="$REPO_ROOT/tools"

echo "🚀 Starting wiki ingestion for: $PROJECT_NAME"
echo ""

# Step 1: Pull project from Drive
echo "📥 Pulling project from Google Drive..."
cd "$REPO_ROOT"
python3 "$SCRIPT_DIR/sync_project.py" pull "$PROJECT_NAME"
echo "✓ Project pulled"
echo ""

# Step 2: Verify project structure
if [ ! -d "/tmp/wiki-project" ]; then
    echo "❌ Error: /tmp/wiki-project directory not found after pull"
    exit 1
fi

if [ ! -f "/tmp/wiki-project/PROJECT.md" ]; then
    echo "❌ Error: PROJECT.md not found in /tmp/wiki-project"
    exit 1
fi

echo "📋 Project structure verified"
echo ""

# Step 3: Load and display prompt
PROMPT_FILE="$SCRIPT_DIR/wiki_prompt.md"
if [ ! -f "$PROMPT_FILE" ]; then
    echo "❌ Error: $PROMPT_FILE not found"
    exit 1
fi

PROMPT_TEXT=$(cat "$PROMPT_FILE")

# Step 4: Launch Claude with the ingestion prompt
echo "🤖 Launching Claude for ingestion workflow..."
echo "   Project: $PROJECT_NAME"
echo "   Working directory: /tmp/wiki-project/"
echo ""
echo "───────────────────────────────────────────────────────"
echo ""

export WIKI_PROJECT="$PROJECT_NAME"

# Use claude command to run the ingestion with the prompt
claude "$PROMPT_TEXT"

# Step 5: Final push to Drive
echo ""
echo "───────────────────────────────────────────────────────"
echo ""
echo "📤 Performing final push to Google Drive..."
cd "$REPO_ROOT"
python3 "$SCRIPT_DIR/sync_project.py" push "$PROJECT_NAME" || {
    echo "⚠️  Final push encountered issues (may be auth-related)"
    echo "   Please run manually: python3 tools/sync_project.py push $PROJECT_NAME"
}

echo ""
echo "✅ Wiki ingestion workflow complete for: $PROJECT_NAME"
echo ""
echo "📍 Project data: /tmp/wiki-project/"
echo "📝 Check wiki/log.md for ingestion history"
echo "🔗 Run status command: cd /tmp/wiki-project && python3 tools/sync_project.py status"
