#!/usr/bin/env python3
"""
Autonomous ingest pipeline for LLM Wiki Agent.
Processes all files in raw/, extracts content, calls Anthropic API,
generates wiki pages, and maintains index/log.
"""

import os
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional
import anthropic

try:
    import fitz  # pymupdf
except ImportError:
    fitz = None


class WikiIngestPipeline:
    def __init__(self, project_root: Path = Path(".")):
        self.project_root = project_root
        self.raw_dir = project_root / "raw"
        self.wiki_dir = project_root / "wiki"
        self.log_file = self.wiki_dir / "log.md"
        self.index_file = self.wiki_dir / "index.md"

        # Try to get API key from environment
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            # If not found, try initializing without explicit key (will use default auth)
            try:
                self.client = anthropic.Anthropic()
            except Exception as e:
                raise ValueError(
                    f"ANTHROPIC_API_KEY environment variable not set and default auth failed: {e}"
                )
        else:
            self.client = anthropic.Anthropic(api_key=api_key)

        self.ingested_files = set()
        self._load_ingested_files()

    def _load_ingested_files(self):
        """Parse log.md to find already-ingested files."""
        if not self.log_file.exists():
            return
        content = self.log_file.read_text()
        # Extract filenames from log entries like "**Source**: `raw/<filename>`"
        pattern = r"\*\*Source\*\*:\s*`raw/([^`]+)`"
        self.ingested_files = set(re.findall(pattern, content))

    def _get_unprocessed_files(self) -> list[Path]:
        """Find all files in raw/ that haven't been ingested yet."""
        if not self.raw_dir.exists():
            return []

        unprocessed = []
        for file_path in self.raw_dir.rglob("*"):
            if file_path.is_file() and file_path.name not in [
                ".gitkeep",
                ".DS_Store",
            ]:
                rel_path = file_path.relative_to(self.raw_dir)
                if str(rel_path) not in self.ingested_files:
                    unprocessed.append(file_path)
        return sorted(unprocessed)

    def _extract_text_from_pdf(self, file_path: Path) -> str:
        """Extract text from PDF using pymupdf."""
        if fitz is None:
            raise ImportError("pymupdf not installed. Run: pip install pymupdf")

        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text

    def _read_file_content(self, file_path: Path) -> str:
        """Read content from file (PDF or text)."""
        if file_path.suffix.lower() == ".pdf":
            return self._extract_text_from_pdf(file_path)
        else:
            try:
                return file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                return file_path.read_text(encoding="latin-1")

    def _chunk_content(self, content: str, max_chunk_size: int = 20000) -> list[str]:
        """Split large content into chunks with overlap."""
        if len(content) <= max_chunk_size:
            return [content]

        chunks = []
        overlap = 1000
        start = 0

        while start < len(content):
            end = start + max_chunk_size
            chunk = content[start:end]
            chunks.append(chunk)
            start = end - overlap

        return chunks

    def _get_existing_wiki_context(self) -> str:
        """Read existing wiki pages to provide context to the API."""
        context = ""

        # Read index to see what exists
        if self.index_file.exists():
            context += "# Current Wiki Index\n\n"
            context += self.index_file.read_text()
            context += "\n\n"

        # Sample recent log entries
        if self.log_file.exists():
            context += "# Recent Operations\n\n"
            lines = self.log_file.read_text().split("\n")
            context += "\n".join(lines[-50:])

        return context

    def _call_claude_api(
        self, file_name: str, content: str, chunk_num: int = 1, total_chunks: int = 1
    ) -> str:
        """Call Anthropic API to analyze document and generate wiki content."""
        wiki_context = self._get_existing_wiki_context()

        chunk_info = (
            f"(chunk {chunk_num}/{total_chunks})"
            if total_chunks > 1
            else ""
        )

        prompt = f"""You are an LLM Wiki Agent maintaining a personal knowledge base.

Your task: analyze the following document and generate structured wiki pages according to this format.

## Format Requirements:
1. Source page (wiki/sources/<slug>.md):
   - Title, Source file, Ingested date, Type
   - Summary (2-4 sentences)
   - Key claims (bullet list)
   - Entities mentioned (comma-separated with [[links]])
   - Concepts mentioned (comma-separated with [[links]])
   - Raw notes (any additional info)

2. Entity pages (wiki/entities/<slug>.md) for each key person, place, organization:
   - Entity Name and Type
   - Overview section
   - Timeline section (if applicable)
   - Appearances section
   - Related section

3. Concept pages (wiki/concepts/<slug>.md) for key concepts:
   - Concept Name
   - Definition section
   - Examples section (linking sources)
   - Related concepts section

Rules:
- Use lowercase-hyphenated names for file slugs
- Always use [[page-name]] links between related pages
- Never fabricate information
- If content contradicts existing wiki, note it as ⚠ Contradiction
- Keep summaries concise

## Current Wiki State:
{wiki_context}

## Document to Analyze {chunk_info}:
**File**: {file_name}

{content[:15000]}...

Now generate the wiki pages in JSON format:

{{
  "source_page": {{
    "slug": "...",
    "filename": "wiki/sources/<slug>.md",
    "content": "# Title\\n\\n**Source**: `raw/{file_name}`\\n..."
  }},
  "entities": [
    {{
      "slug": "...",
      "name": "...",
      "type": "Person/Place/Organization/Product",
      "content": "# Name\\n\\n**Type**: Type\\n..."
    }}
  ],
  "concepts": [
    {{
      "slug": "...",
      "name": "...",
      "content": "# Name\\n\\n## Definition\\n..."
    }}
  ],
  "contradictions": ["description of any contradictions found"],
  "notes": "additional processing notes"
}}

Generate only valid JSON output. Include only pages that have substantial content."""

        response = self.client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            messages=[{"role": "user", "content": prompt}],
        )

        return response.content[0].text

    def _parse_and_write_pages(self, api_response: str, file_path: Path) -> dict:
        """Parse API response and write wiki pages."""
        try:
            # Extract JSON from response
            json_match = re.search(r"\{.*\}", api_response, re.DOTALL)
            if not json_match:
                return {
                    "error": "No JSON found in response",
                    "pages_written": [],
                    "pages_updated": [],
                }

            data = json.loads(json_match.group())
        except json.JSONDecodeError as e:
            return {
                "error": f"JSON parse error: {e}",
                "pages_written": [],
                "pages_updated": [],
            }

        result = {
            "pages_written": [],
            "pages_updated": [],
            "contradictions": data.get("contradictions", []),
        }

        # Write source page
        if "source_page" in data:
            source = data["source_page"]
            source_path = self.wiki_dir / source["filename"]
            source_path.parent.mkdir(parents=True, exist_ok=True)
            source_path.write_text(source["content"])
            result["pages_written"].append(source["slug"])

        # Write entity pages
        for entity in data.get("entities", []):
            entity_path = self.wiki_dir / "entities" / f"{entity['slug']}.md"
            entity_path.parent.mkdir(parents=True, exist_ok=True)

            if entity_path.exists():
                result["pages_updated"].append(entity["slug"])
            else:
                result["pages_written"].append(entity["slug"])

            entity_path.write_text(entity["content"])

        # Write concept pages
        for concept in data.get("concepts", []):
            concept_path = self.wiki_dir / "concepts" / f"{concept['slug']}.md"
            concept_path.parent.mkdir(parents=True, exist_ok=True)

            if concept_path.exists():
                result["pages_updated"].append(concept["slug"])
            else:
                result["pages_written"].append(concept["slug"])

            concept_path.write_text(concept["content"])

        return result

    def _update_log(
        self,
        file_rel_path: str,
        pages_written: list[str],
        pages_updated: list[str],
        contradictions: list[str],
        notes: str = "",
    ):
        """Append entry to wiki/log.md."""
        today = datetime.now().strftime("%Y-%m-%d")

        entry = f"## {today} — ingest {file_rel_path}\n\n"
        entry += f"- **Source**: `raw/{file_rel_path}`\n"

        if pages_written:
            entry += f"- **Pages written**: {', '.join(f'[[{p}]]' for p in pages_written)}\n"
        if pages_updated:
            entry += f"- **Pages updated**: {', '.join(f'[[{p}]]' for p in pages_updated)}\n"
        if contradictions:
            entry += f"- **Contradictions flagged**: {', '.join(contradictions)}\n"
        if notes:
            entry += f"- **Notes**: {notes}\n"

        entry += "\n"

        if not self.log_file.exists():
            self.log_file.write_text("# Operation Log\n\nAppend-only.\n\n---\n\n")

        current = self.log_file.read_text()
        self.log_file.write_text(current + entry)

    def _update_index(self):
        """Regenerate wiki/index.md based on current wiki pages."""
        sources = []
        entities = []
        concepts = []
        synthesis = []
        contradictions = []

        # Scan wiki directories
        sources_dir = self.wiki_dir / "sources"
        if sources_dir.exists():
            for f in sorted(sources_dir.glob("*.md")):
                slug = f.stem
                sources.append(f"- [[{slug}]]")

        entities_dir = self.wiki_dir / "entities"
        if entities_dir.exists():
            for f in sorted(entities_dir.glob("*.md")):
                slug = f.stem
                entities.append(f"- [[{slug}]]")

        concepts_dir = self.wiki_dir / "concepts"
        if concepts_dir.exists():
            for f in sorted(concepts_dir.glob("*.md")):
                slug = f.stem
                concepts.append(f"- [[{slug}]]")

        synthesis_dir = self.wiki_dir / "synthesis"
        if synthesis_dir.exists():
            for f in sorted(synthesis_dir.glob("*.md")):
                slug = f.stem
                synthesis.append(f"- [[{slug}]]")

        # Parse contradictions from log
        if self.log_file.exists():
            log_content = self.log_file.read_text()
            contra_matches = re.findall(
                r"\*\*Contradictions flagged\*\*:\s*(.+)", log_content
            )
            for match in contra_matches:
                contradictions.append(f"- {match}")

        today = datetime.now().strftime("%Y-%m-%d")
        total_pages = (
            len(sources) + len(entities) + len(concepts) + len(synthesis)
        )

        index = f"""# Wiki Index

**Last updated**: {today}
**Total pages**: {total_pages}

## Sources

{chr(10).join(sources) if sources else '*(none yet)*'}

## Entities

{chr(10).join(entities) if entities else '*(none yet)*'}

## Concepts

{chr(10).join(concepts) if concepts else '*(none yet)*'}

## Synthesis

{chr(10).join(synthesis) if synthesis else '*(none yet)*'}

## Open contradictions

{chr(10).join(contradictions) if contradictions else '*(none)*'}
"""

        self.index_file.write_text(index)

    def process_file(self, file_path: Path) -> bool:
        """Process a single file and return True if successful."""
        rel_path = file_path.relative_to(self.raw_dir)
        print(f"\n📄 Processing: {rel_path}")

        try:
            content = self._read_file_content(file_path)
            print(f"   ✓ Extracted {len(content)} characters")
        except Exception as e:
            print(f"   ✗ Failed to read: {e}")
            return False

        # Process in chunks if necessary
        chunks = self._chunk_content(content)
        all_written = []
        all_updated = []
        all_contradictions = []

        for chunk_num, chunk in enumerate(chunks, 1):
            print(f"   → Processing chunk {chunk_num}/{len(chunks)}...")

            try:
                api_response = self._call_claude_api(
                    str(rel_path), chunk, chunk_num, len(chunks)
                )
                result = self._parse_and_write_pages(api_response, file_path)

                if "error" in result:
                    print(f"     ⚠ {result['error']}")
                else:
                    all_written.extend(result["pages_written"])
                    all_updated.extend(result["pages_updated"])
                    all_contradictions.extend(result["contradictions"])
                    print(
                        f"     ✓ {len(result['pages_written'])} pages written, "
                        f"{len(result['pages_updated'])} updated"
                    )
            except Exception as e:
                print(f"     ✗ API call failed: {e}")
                return False

        # Update log and index
        self._update_log(
            str(rel_path),
            all_written,
            all_updated,
            all_contradictions,
        )
        self._update_index()

        print(f"   ✓ Complete: {len(all_written)} new pages, {len(all_updated)} updated")
        return True

    def run(self):
        """Run the ingest pipeline for all unprocessed files."""
        print("\n🚀 LLM Wiki Agent — Ingest Pipeline\n")

        unprocessed = self._get_unprocessed_files()

        if not unprocessed:
            print("✓ All files in raw/ have been ingested.")
            return

        print(f"Found {len(unprocessed)} file(s) to process:\n")

        for file_path in unprocessed:
            self.process_file(file_path)

        print("\n✓ Ingest pipeline complete.\n")


if __name__ == "__main__":
    pipeline = WikiIngestPipeline()
    pipeline.run()
