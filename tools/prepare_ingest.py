#!/usr/bin/env python3
"""
Prepare all documents for ingestion by extracting and organizing content.
Output a JSON file that can be processed directly by Claude.
"""

import json
import re
from pathlib import Path
from typing import Optional

try:
    import fitz  # pymupdf
except ImportError:
    fitz = None


def extract_text_from_pdf(file_path: Path) -> tuple[str, int]:
    """Extract text from PDF. Returns (text, page_count)."""
    if fitz is None:
        return "", 0

    try:
        doc = fitz.open(file_path)
        text = ""
        page_count = len(doc)
        for page in doc:
            text += page.get_text()
        doc.close()
        return text, page_count
    except Exception as e:
        return f"[Error: {e}]", 0


def extract_text_from_file(file_path: Path) -> str:
    """Extract text from any file."""
    suffix = file_path.suffix.lower()

    if suffix == ".pdf":
        text, _ = extract_text_from_pdf(file_path)
        return text
    elif suffix == ".docx":
        try:
            return file_path.read_bytes().decode('utf-8', errors='ignore')
        except:
            return "[DOCX file - binary format]"
    else:
        try:
            return file_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                return file_path.read_text(encoding="latin-1")
            except:
                return "[Unable to extract text]"


def prepare_documents(raw_dir: Path = Path("raw")) -> dict:
    """Prepare all documents with full content."""
    documents = []

    for file_path in sorted(raw_dir.rglob("*")):
        if not file_path.is_file() or file_path.name in [".gitkeep", ".DS_Store", "debug.log"]:
            continue

        rel_path = str(file_path.relative_to(raw_dir))

        # Determine file type
        suffix = file_path.suffix.lower()
        if suffix == ".pdf":
            file_type = "PDF"
        elif suffix == ".docx":
            file_type = "DOCX"
        elif suffix in [".htm", ".html"]:
            file_type = "HTML"
        elif suffix == ".txt":
            file_type = "Text"
        else:
            file_type = suffix.upper() or "Unknown"

        # Extract content
        content = extract_text_from_file(file_path)
        file_size = file_path.stat().st_size

        documents.append({
            "name": file_path.name,
            "path": rel_path,
            "type": file_type,
            "size_kb": file_size / 1024,
            "content_length": len(content),
            "content": content[:15000] if len(content) > 15000 else content  # First 15k chars
        })

    return {
        "total_documents": len(documents),
        "documents": documents
    }


if __name__ == "__main__":
    raw_dir = Path(".") / "raw"
    data = prepare_documents(raw_dir)

    # Write to JSON file for processing
    output_file = Path("tools/ingest_data.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"✓ Prepared {data['total_documents']} documents")
    print(f"✓ Written to {output_file}")

    # Print file list
    for doc in data['documents']:
        print(f"  - {doc['name']} ({doc['type']}, {doc['size_kb']:.1f}KB)")
