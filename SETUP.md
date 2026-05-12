# Setup Guide — LLM Wiki

Complete setup for running LLM Wiki on your machine.

---

## Prerequisites

- **Claude Code** (the CLI) — [Install here](https://claude.com/claude-code)
- **Python 3.8+** — `python3 --version`
- **Git** (to clone this repo)

---

## Step 1: Clone this repository

```bash
git clone https://github.com/yourusername/llm-wiki-template.git
cd llm-wiki-template
```

---

## Step 2: Set up Google Drive connection

### Option A: Use Claude Code's built-in MCP (Recommended)

No manual setup needed! Claude Code comes with Google Drive integration.

In any Claude Code session, just run:
```
/mcp
```

Then select **"claude.ai Google Drive"** and authorize your Google account.

**That's it.** You can now close Claude Code.

### Option B: Manual OAuth2 (if Option A doesn't work)

1. Go to [myaccount.google.com/permissions](https://myaccount.google.com/permissions)
2. Look for "Third-party apps with account access"
3. Add/authorize Claude Code for Google Drive access

---

## Step 3: Create the LLM-Wiki folder structure on Google Drive

1. **Create root folder**: On Google Drive, create a folder named **LLM-Wiki**
2. **Copy folder ID**: Right-click the folder → Share → Copy ID
3. **Update projects.md**: Paste the ID as the Root LLM-Wiki folder ID (see Step 5)

---

## Step 4: Create your first project

In Google Drive, inside **LLM-Wiki/**:

1. **Create project folder**: Name it (e.g., `My-Project`, `Research-2026`)
2. **Add PROJECT.md**: Create a text file with:
   ```markdown
   # Project Name
   
   ## Domain
   What field/topic is this knowledge base about?
   
   ## Goal
   What are you trying to achieve?
   
   ## Source Types
   What kinds of documents will you be adding?
   ```
3. **Create raw/ folder**: Where you'll put source files (PDFs, markdown, docs, etc.)
4. **Copy folder ID**: Right-click project folder → Share → Copy ID

---

## Step 5: Register your project

Edit `projects.md` in this repo:

```markdown
| Name | Drive Folder ID | Status | Last Session |
|------|-----------------|--------|--------------|
| My-Project | [PASTE-FOLDER-ID-HERE] | active | — |
```

And update the Root section:
```markdown
## Root
- **LLM-Wiki**: [PASTE-ROOT-FOLDER-ID-HERE]
```

---

## Step 6: Set your Anthropic API key

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

You can find your API key at [console.anthropic.com](https://console.anthropic.com/api_keys).

(Optional: Add to your shell profile `~/.bashrc` or `~/.zshrc` to persist across sessions)

---

## Step 7: Start your first wiki ingestion

```bash
./tools/wiki.sh My-Project
```

The script will:
1. ✅ Pull your project from Drive
2. ✅ Ingest all files in `raw/`
3. ✅ Build wiki pages with cross-references
4. ✅ Push everything back to Drive

---

## Troubleshooting

### "Permission denied" when running wiki.sh

Make the script executable:
```bash
chmod +x ./tools/wiki.sh
```

### "Claude command not found"

Install Claude Code:
```bash
# If using npm:
npm install -g claude

# Or visit: https://claude.com/claude-code
```

### "Project not found in projects.md"

Make sure you:
1. Added the project to `projects.md` with the correct folder ID
2. Committed the change to git
3. Used the exact project name when calling `./tools/wiki.sh My-Project`

### "Google Drive authentication failed"

Try re-authenticating:
```
/mcp
```
Select "claude.ai Google Drive" again and re-authorize.

If that doesn't work, check your Drive permissions and make sure the LLM-Wiki folder is accessible to your Google account.

### "sync_project.py: Service Accounts do not have storage quota"

This means the code is trying to use service account credentials instead of your personal account.

**Fix**: Make sure you've authenticated via `/mcp` in Claude Code. The personal OAuth2 tokens take precedence.

If you still have issues, set this environment variable:
```bash
unset GOOGLE_SERVICE_ACCOUNT
```

---

## Tips

- **Start small**: Add 1-2 documents first, get comfortable with the workflow, then scale
- **Use Obsidian**: Download the `wiki/` folder locally and open it in [Obsidian](https://obsidian.md/) for graph view and backlinks
- **Name projects clearly**: Use dashes (not spaces) — e.g., `Product-Analysis`, `Q1-Research`, `Book-Notes`
- **Keep PROJECT.md updated**: This guides Claude on how to interpret your sources
- **Check the log**: After each ingestion, review `wiki/log.md` to understand what changed

---

## Getting help

- Check `README.md` for workflow overview
- See `CLAUDE.md` for detailed agent instructions
- Review existing wiki pages in another project for examples

Happy knowledge building! 🧠
