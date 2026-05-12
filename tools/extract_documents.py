#!/usr/bin/env python3
"""
Extract content from all documents in raw/ and output structured JSON.
This will be processed by Claude directly.
"""

import json
import os
from pathlib import Path
from typing import Optional

try:
    import fitz  # pymupdf
except ImportError:
    fitz = None


def extract_text_from_pdf(file_path: Path) -> str:
    """Extract text from PDF using pymupdf."""
    if fitz is None:
        raise ImportError("pymupdf not installed. Run: pip install pymupdf")

    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text[:10000]  # Limit to first 10k chars for preview
    except Exception as e:
        return f"[Error extracting PDF: {e}]"


def extract_text_from_txt(file_path: Path) -> str:
    """Extract text from text file."""
    try:
        return file_path.read_text(encoding="utf-8")[:10000]
    except UnicodeDecodeError:
        return file_path.read_text(encoding="latin-1")[:10000]


def extract_text_from_htm(file_path: Path) -> str:
    """Extract text from HTML file."""
    try:
        return file_path.read_text(encoding="utf-8")[:10000]
    except UnicodeDecodeError:
        return file_path.read_text(encoding="latin-1")[:10000]


def extract_text_from_docx(file_path: Path) -> str:
    """Extract text from DOCX (limited, no library dependency)."""
    try:
        # Try to extract text without python-docx
        return file_path.read_text(encoding="utf-8", errors="ignore")[:10000]
    except:
        return "[DOCX file - unable to extract without python-docx]"


def extract_all_documents(raw_dir: Path = Path("raw")) -> dict:
    """Extract all documents and return structured data."""
    documents = {}

    for file_path in sorted(raw_dir.rglob("*")):
        if not file_path.is_file() or file_path.name in [".gitkeep", ".DS_Store"]:
            continue

        rel_path = str(file_path.relative_to(raw_dir))

        text = ""
        file_type = "unknown"

        if file_path.suffix.lower() == ".pdf":
            text = extract_text_from_pdf(file_path)
            file_type = "pdf"
        elif file_path.suffix.lower() in [".txt", ".md"]:
            text = extract_text_from_txt(file_path)
            file_type = "text"
        elif file_path.suffix.lower() in [".htm", ".html"]:
            text = extract_text_from_htm(file_path)
            file_type = "html"
        elif file_path.suffix.lower() == ".docx":
            text = extract_text_from_docx(file_path)
            file_type = "docx"
        elif file_path.suffix.lower() == ".log":
            text = extract_text_from_txt(file_path)
            file_type = "log"

        documents[rel_path] = {
            "type": file_type,
            "size_bytes": file_path.stat().st_size,
            "preview": text[:2000] if text else "[No content extracted]"
        }

    return documents


if __name__ == "__main__":
    raw_dir = Path(".") / "raw"
    documents = extract_all_documents(raw_dir)

    print(json.dumps({
        "total_files": len(documents),
        "documents": documents
    }, indent=2, ensure_ascii=False))
