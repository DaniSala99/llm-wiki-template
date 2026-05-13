# 🧠 LLM Wiki Agent

A reusable project template for building and maintaining AI-powered personal knowledge bases with Claude Code. Drop your sources, get a structured, interlinked wiki that compounds over time.

---

## The idea

Most LLM-document tools (RAG, NotebookLM, ChatGPT file uploads) retrieve from raw sources at query time — rediscovering knowledge from scratch on every question. Nothing accumulates.

This template does something different: Claude **builds and maintains a persistent wiki** between you and your raw sources. When you add a new document, Claude doesn't just index it — it reads it, extracts key information, and integrates it into the existing wiki: updating entity pages, flagging contradictions, strengthening the evolving synthesis.

The wiki is a compounding artifact. The cross-references are already there. The contradictions have already been flagged. Every source you add makes it richer.

---

## Quickstart

### 1. Set up Google Drive authentication

**Option A: Use Claude Code MCP (Recommended)**

No setup needed! Claude Code comes with built-in Google Drive integration.

In Claude Code, just run:
```
/mcp
```

Select **"claude.ai Google Drive"** and authorize your Google account. Done!

**Option B: Manual OAuth2 setup** (if Option A doesn't work)

1. Go to [myaccount.google.com/permissions](https://myaccount.google.com/permissions)
2. Look for "Third-party apps with account access" and authorize Claude Code
3. Or run: `gcloud auth application-default login`

### 2. Set your Anthropic API key

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

### 3. Create a project on Google Drive

1. On Google Drive, create or find the **LLM-Wiki** root folder
2. Inside it, create a new folder for your project (e.g., `My-Project`)
3. Inside your project folder, create:
   - **PROJECT.md** — your project context (what domain, goal, source types)
   - **raw/** — folder for your source files (PDFs, markdown, docs, etc.)
   - Claude will auto-create **wiki/** when you start ingesting

Example structure:
```
LLM-Wiki/
└── My-Project/
    ├── PROJECT.md
    ├── raw/
    │   ├── document1.pdf
    │   └── document2.md
    └── wiki/ ← Created automatically
```

### 4. Register your project in projects.md

Edit `projects.md` in this repo and add a row with:
- **Name**: Your project name (e.g., `My-Project`)
- **Drive Folder ID**: The folder ID from Drive (right-click → Share → copy ID)
- **Status**: `active` or `archived`

### 5. Start the wiki workflow

In Claude Code, run:

```bash
python3 tools/sync_project.py pull My-Project
```

Claude will:
1. Pull your project from Drive to `/tmp/wiki-project/`
2. Read PROJECT.md and understand your domain
3. Download all sources and existing wiki pages
4. You can now query, ingest, or update the wiki interactively

After your work:

```bash
python3 tools/sync_project.py push My-Project
```

That's it! Your changes are now on Drive.

---

## Main workflow

```bash
# Pull your project from Drive
python3 tools/sync_project.py pull My-Project

# Work interactively in Claude Code:
# - Ingest sources: ingest raw/file.pdf
# - Query the wiki: [any question]
# - Check health: lint
# - View status: status

# Push your changes back to Drive
python3 tools/sync_project.py push My-Project
```

## Interactive commands (inside Claude Code)

Once the wiki is pulled, you can use these:

| Command | What happens |
|---|---|
| `ingest raw/file.pdf` | Claude reads the source, discusses takeaways, writes wiki pages, updates cross-references |
| `ingest raw/` | Batch-ingest all un-ingested files from raw/ |
| `[any question]` | Claude searches the wiki and answers with citations; offers to save analyses |
| `lint` | Health check: contradictions, orphan pages, stale claims, missing cross-references |
| `status` | Overview of wiki state, un-ingested sources, recent operations |

---

## Repository structure

This repo is **stateless**. All project data lives on Google Drive.

```
llm-wiki-template/          ← This repo (universal tools)
├── CLAUDE.md               ← Agent instructions
├── projects.md             ← List of projects on Google Drive
├── tools/
│   ├── drive.py            ← Google Drive API wrapper
│   └── sync_project.py     ← Pull/push projects to Drive
├── .devcontainer/          ← Codespace config
└── .gitignore              ← Excludes /tmp/, cache, etc.

# On Google Drive:
LLM-Wiki/                    ← Root folder (shared with service account)
└── Your-Project/
    ├── PROJECT.md          ← Your project context
    ├── raw/                ← Your source files (PDFs, markdown, etc.)
    └── wiki/               ← Claude builds and maintains this
        ├── index.md        ← Full catalog
        ├── log.md          ← Append-only operation log
        ├── sources/        ← One page per source
        ├── entities/       ← People, companies, products, places
        ├── concepts/       ← Ideas, frameworks, terminology
        └── synthesis/      ← Cross-source analyses and saved queries
```

**Flow**: 
1. At session start: `sync_project.py pull` downloads project from Drive → `/tmp/wiki-project/`
2. Claude works in `/tmp/wiki-project/` 
3. At end of session: `sync_project.py push` uploads wiki/ back to Drive
4. `/tmp/` is never committed to this repo

---

## How a session looks

```bash
$ claude

# Claude downloads from Drive, orients itself
> "Project: Fintech Analysis | Wiki pages: 23 | Last op: 2026-05-10 ingest | 3 sources pending"

# Add a new source (uploaded to raw/ on Drive)
ingest raw/q1-2026-report.pdf

# Claude discusses takeaways, then:
# → writes wiki/sources/q1-2026-report.md
# → updates wiki/entities/company-x.md (new funding data)
# → updates wiki/concepts/embedded-finance.md (new example)
# → flags contradiction with wiki/entities/company-y.md
# → updates index.md and log.md
# → pushes changes to Drive

# Ask anything
What are the main competitive dynamics identified so far?

# Claude searches wiki, answers with citations, offers to save the synthesis
# Saves to wiki/synthesis/ and pushes to Drive

# Periodic health check
lint

# At session end, all wiki changes are automatically on Drive
```

---

## Why this works

The tedious part of maintaining a knowledge base isn't the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims. Humans abandon wikis because the maintenance burden grows faster than the perceived value.

Claude doesn't get bored, doesn't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.

Your job: curate sources, ask good questions, think about what it all means.  
Claude's job: everything else.

---

## Use cases

- **Research** — papers, reports, articles on a topic over weeks or months
- **Competitive analysis** — tracking players, strategies, and market signals
- **Due diligence** — building a structured picture from heterogeneous documents
- **Reading a book** — filing each chapter, building pages for characters, themes, plot threads
- **Meeting & project knowledge** — fed by transcripts, Slack exports, project docs
- **Personal** — goals, health, self-improvement — filing journal entries and articles over time

---

## Tips

- **Obsidian** as a reading interface for the wiki gives you graph view, backlinks, and live preview. Point it at the `wiki/` directory.
- **Obsidian Web Clipper** (browser extension) converts web articles to markdown — fast way to get sources into `raw/`.
- The wiki is a plain git repo. You get version history, branching, and diffing for free. Commit often.
- Start with `ingest` on your most important sources first, then let the wiki grow organically.
- Save good query answers back into `wiki/synthesis/` — your explorations should compound too.

---

## Status

✅ **Production-ready**. The template has been tested end-to-end:
- Google Drive authentication (MCP-based OAuth2)
- File ingestion and wiki page generation
- Cross-reference and contradiction detection
- Multi-folder wiki structure (procedures, checklists, legal framework, regional docs, national system)
- Automatic push/pull synchronization with Drive
- Example project: CFMR Lombardia (22 markdown files from 550 pages of PDF/DOCX documentation)

See [CLAUDE.md](CLAUDE.md) for detailed agent instructions, [SETUP.md](SETUP.md) for step-by-step configuration.

---

## Credits

Based on the [LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) — an idea for building personal knowledge bases using LLMs as maintainers rather than retrievers.
