#!/bin/bash
set -e

# Wiki automation script - orchestrates full ingestion workflow
# Usage: ./tools/wiki.sh <project-name>
# Example: ./tools/wiki.sh My-Project

PROJECT_NAME="${1:-}"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT_DIR="$REPO_ROOT/tools"

# Helper functions
print_header() {
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  $1"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
}

error_exit() {
    echo ""
    echo "❌ $1"
    echo ""
    exit 1
}

# Check prerequisites
check_prerequisites() {
    print_header "Checking prerequisites"

    if ! command -v python3 &> /dev/null; then
        error_exit "python3 is required but not installed"
    fi

    if ! command -v claude &> /dev/null; then
        error_exit "claude CLI is required. Install from: https://claude.com/claude-code"
    fi

    if [ ! -f "$REPO_ROOT/projects.md" ]; then
        error_exit "projects.md not found in repo root"
    fi

    if [ ! -f "$SCRIPT_DIR/sync_project.py" ]; then
        error_exit "sync_project.py not found in tools/"
    fi

    if [ ! -f "$SCRIPT_DIR/wiki_prompt.md" ]; then
        error_exit "wiki_prompt.md not found in tools/"
    fi

    echo "✓ All prerequisites met"
    echo ""
}

# Main workflow
main() {
    if [ -z "$PROJECT_NAME" ]; then
        echo "🧠 LLM Wiki — Automatic ingestion workflow"
        echo ""
        echo "Usage: $0 <project-name>"
        echo "Example: $0 My-Project"
        echo ""
        echo "Available projects (from projects.md):"
        grep "^| " "$REPO_ROOT/projects.md" | tail -n +2 | awk -F'|' '{print "  • " $2}' | sed 's/ //g'
        echo ""
        exit 0
    fi

    check_prerequisites

    print_header "LLM Wiki Ingestion: $PROJECT_NAME"

    # Step 1: Pull from Drive
    echo "📥 Pulling project from Google Drive..."
    cd "$REPO_ROOT"
    if ! python3 "$SCRIPT_DIR/sync_project.py" pull "$PROJECT_NAME" 2>&1; then
        error_exit "Failed to pull project. Check that the project exists in projects.md and you have Drive access."
    fi
    echo "✓ Project pulled to /tmp/wiki-project/"
    echo ""

    # Step 2: Verify project structure
    if [ ! -d "/tmp/wiki-project" ]; then
        error_exit "/tmp/wiki-project directory not created"
    fi

    if [ ! -f "/tmp/wiki-project/PROJECT.md" ]; then
        error_exit "PROJECT.md not found. Check your Drive project structure."
    fi

    if [ ! -d "/tmp/wiki-project/raw" ]; then
        echo "⚠️  No raw/ folder found. Create one and add source files to begin ingestion."
    fi

    echo "📋 Project structure verified"
    echo ""

    # Step 3: Check PROJECT.md content
    if grep -q "^## " "/tmp/wiki-project/PROJECT.md"; then
        echo "📖 Project context loaded from PROJECT.md"
        echo ""
    else
        echo "⚠️  PROJECT.md appears empty. Consider filling in project details:"
        echo "   - Domain: What field/topic is this?"
        echo "   - Goal: What are you trying to achieve?"
        echo "   - Source types: What kinds of documents are you adding?"
        echo ""
    fi

    # Step 4: Launch Claude with ingestion prompt
    print_header "Launching Claude for ingestion"

    export WIKI_PROJECT="$PROJECT_NAME"

    # Load and substitute prompt
    PROMPT_TEXT=$(cat "$SCRIPT_DIR/wiki_prompt.md" | envsubst)

    # Launch Claude
    claude "$PROMPT_TEXT"

    # Step 5: Final push to Drive
    print_header "Final sync to Google Drive"

    cd "$REPO_ROOT"
    if python3 "$SCRIPT_DIR/sync_project.py" push "$PROJECT_NAME" 2>&1; then
        echo ""
        echo "✅ Wiki successfully synced to Drive!"
        echo ""
        echo "📊 Wiki location:"
        echo "   Google Drive → LLM-Wiki → $PROJECT_NAME → wiki/"
        echo ""
        echo "📝 Check /tmp/wiki-project/wiki/log.md for ingestion history"
        echo ""
        echo "🔄 To sync again in a new session:"
        echo "   $0 $PROJECT_NAME"
        echo ""
    else
        echo ""
        echo "⚠️  Final sync encountered issues (likely auth-related)"
        echo "    The wiki is ready locally at /tmp/wiki-project/wiki/"
        echo ""
        echo "    To sync manually to Drive:"
        echo "    python3 $SCRIPT_DIR/sync_project.py push $PROJECT_NAME"
        echo ""
    fi
}

main
