# Wiki Ingestion Prompt

You are the maintainer of a personal knowledge base (wiki) built from raw source documents. Follow the CLAUDE.md instructions in the repository for session startup and ingestion workflows.

## Task

Complete the full wiki ingestion workflow for the project specified in the environment variable `WIKI_PROJECT`.

## Instructions

1. **Setup** (do immediately):
   - Set working directory to `/tmp/wiki-project/`
   - Read `PROJECT.md` to understand the domain
   - Read `wiki/index.md` and last 20 lines of `wiki/log.md` to know current state
   - List `raw/` directory and identify files not yet in `wiki/log.md` — these are pending

2. **Batch Ingest** (process all pending files):
   - For each pending file in `raw/`:
     - Extract full text using appropriate tool (pdfplumber for PDFs, etc.)
     - Read content fully before proceeding
     - Discuss 3–5 key takeaways with the user
     - Create `wiki/sources/<slug>.md` with structured summary
     - Create or update `wiki/entities/<slug>.md` for each key entity
     - Create or update `wiki/concepts/<slug>.md` for each key concept
     - Flag any contradictions with existing wiki content
     - Add cross-references using `[[page-name]]` links
   - After each ingest:
     - Update `wiki/index.md` (add new pages)
     - Append to `wiki/log.md` (one entry per operation)
     - **Push to Drive**: `python3 /workspaces/llm-wiki-template/tools/sync_project.py push $WIKI_PROJECT`

3. **Final Steps** (when all files ingested):
   - Run lint: check for contradictions, orphan pages, stale claims, missing links, empty sections
   - Fix any issues found (ask user which fixes to apply)
   - Final push to Drive: `python3 /workspaces/llm-wiki-template/tools/sync_project.py push $WIKI_PROJECT`
   - Print status summary

## Notes

- Never fabricate information — only include what's in sources
- Always cite wiki pages inline as `[[page-name]]`
- Prefer updating existing pages over creating duplicates
- Cross-reference liberally between pages
- If DEWETRA, GESTCOM, LIRIS, or similar platforms are mentioned, create concept pages explaining them

## Success criteria

- All files in `raw/` are listed in `wiki/log.md`
- `wiki/index.md` reflects final page count and structure
- No contradictions left unresolved
- All entity/concept pages have cross-references
