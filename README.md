# 🧠 LLM Wiki Agent

A reusable project template for building and maintaining AI-powered personal knowledge bases with Claude Code. Drop your sources, get a structured, interlinked wiki that compounds over time.

---

## The idea

Most LLM-document tools (RAG, NotebookLM, ChatGPT file uploads) retrieve from raw sources at query time — rediscovering knowledge from scratch on every question. Nothing accumulates.

This template does something different: Claude **builds and maintains a persistent wiki** between you and your raw sources. When you add a new document, Claude doesn't just index it — it reads it, extracts key information, and integrates it into the existing wiki: updating entity pages, flagging contradictions, strengthening the evolving synthesis.

The wiki is a compounding artifact. The cross-references are already there. The contradictions have already been flagged. Every source you add makes it richer.

---

## Quickstart

### 1. Create a new project from this template

Click **"Use this template"** on GitHub → create a new repo → open a Codespace.

### 2. Set your Anthropic API key

In your GitHub repo: **Settings → Secrets and variables → Codespaces → New secret**

```
Name:  ANTHROPIC_API_KEY
Value: sk-ant-...
```

### 3. Describe your project

Edit `PROJECT.md` in the root of your new repo (5 minutes):

```markdown
# My Project Name

## Domain
What this project is about.

## Goal
What you want the wiki to help you understand or track.

## Source types
PDF reports, web articles, meeting transcripts, etc.

## Key entities to track
Companies, people, products, concepts — whatever is central to your domain.
```

### 4. Add your sources

Drop any files into `raw/` — PDFs, markdown, text files, exported web articles.

### 5. Start Claude Code and go

```bash
claude
```

Claude will read `PROJECT.md`, orient itself on the current wiki state, and confirm it's ready. Then use the commands below.

---

## Commands

| Command | What happens |
|---|---|
| `ingest raw/file.pdf` | Claude reads the source, discusses takeaways with you, writes wiki pages, updates cross-references |
| `ingest raw/` | Batch-ingest all files in the folder |
| `[any question]` | Claude searches the wiki and answers with citations; offers to save substantial analyses |
| `lint` | Health check: contradictions, orphan pages, stale claims, missing cross-references |
| `status` | Overview of wiki state, un-ingested sources, last operations |

---

## Repository structure

```
your-project/
├── CLAUDE.md               ← Agent instructions (universal, don't edit per-project)
├── PROJECT.md              ← Your project context (edit this for each project)
├── .devcontainer/
│   └── devcontainer.json   ← Codespace config with Claude Code pre-installed
└── raw/                    ← Your sources (PDFs, markdown, text — immutable)
    └── assets/             ← Downloaded images from articles
wiki/                       ← Everything below is written and owned by Claude
    ├── index.md            ← Full catalog of all wiki pages
    ├── log.md              ← Append-only operation log
    ├── sources/            ← One page per ingested source
    ├── entities/           ← People, companies, products, places
    ├── concepts/           ← Ideas, frameworks, terminology
    └── synthesis/          ← Cross-source analyses, comparisons, saved query answers
```

**Rule**: Claude never touches `raw/`. You never write in `wiki/`. Everything in between is collaboration.

---

## How a session looks

```
# Claude orients itself automatically at session start
> "Progetto: Fintech Analysis | Wiki pages: 23 | Last op: 2026-05-10 ingest | 3 sources pending"

# Add a new source
ingest raw/q1-2026-report.pdf

# Claude discusses takeaways, then:
# → writes wiki/sources/q1-2026-report.md
# → updates wiki/entities/company-x.md (new funding data)
# → updates wiki/concepts/embedded-finance.md (new example)
# → flags contradiction with wiki/entities/company-y.md
# → updates index.md and log.md

# Ask anything
What are the main competitive dynamics identified so far?

# Claude searches wiki, answers with citations, offers to save the synthesis

# Periodic health check
lint
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

## Project Status

**Active Project**: Conoscenza Centro Funzionale Monitoraggio Rischi (CFMR)

### Current State (2026-05-12)
- ✅ **30 wiki pages created** from 21 source documents
- ✅ **CFMR procedures documented** (10 operational manuals + 1 decree)
- ✅ **Italian civil protection legislation indexed** (11 legislative documents)
- ✅ **5 key entities** established (CFMR, Regione Lombardia, ARPA, ARIA Spa, Dipartimento PC)
- ✅ **2 core concepts** defined (Allertamento, Sistema Protezione Civile)

### Latest Operation
```
## 2026-05-12 — ingest all raw/ documents (batch 21 sources)
- Pages written: 21 sources + 5 entities + 2 concepts
- Notes: Complete ingestion of CFMR procedures and civil protection legislation
```

---

## Credits

Based on the [LLM Wiki pattern](https://github.com/tobi/llm-wiki) — an idea for building personal knowledge bases using LLMs as maintainers rather than retrievers.
