#!/usr/bin/env python3
"""
Sync LLM Wiki projects between Google Drive and local /tmp/wiki-project/.
"""

import sys
import json
from pathlib import Path
from typing import Optional

from drive import get_client


PROJECT_FILE = Path(__file__).parent.parent / "projects.md"
LOCAL_PROJECT_DIR = Path("/tmp/wiki-project")


def get_project_folder_id(project_name: str) -> Optional[str]:
    """Get Drive folder ID for a project from projects.md."""
    try:
        content = PROJECT_FILE.read_text()
        for line in content.split("\n"):
            if project_name in line and "|" in line:
                parts = [p.strip() for p in line.split("|")]
                if len(parts) >= 3:
                    return parts[2]
    except Exception as e:
        print(f"✗ Error reading projects.md: {e}")
    return None


def pull_project(project_name: str) -> bool:
    """Download project from Drive to /tmp/wiki-project/."""
    client = get_client()
    if not client:
        return False

    folder_id = get_project_folder_id(project_name)
    if not folder_id:
        print(f"✗ Project '{project_name}' not found in projects.md")
        return False

    # Create local directory
    LOCAL_PROJECT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"📥 Pulling {project_name} from Drive...")
    print(f"   Folder ID: {folder_id}")

    # List all files in project folder
    files = client.list_files(folder_id)
    if not files:
        print(f"⚠ No files found in project folder")
        return True

    # Download all files
    for file_info in files:
        file_id = file_info["id"]
        name = file_info["name"]
        mime = file_info.get("mimeType", "")

        # Skip folders (they will be created as needed)
        if mime == "application/vnd.google-apps.folder":
            continue

        local_path = LOCAL_PROJECT_DIR / name
        print(f"   ⬇ {name}...")

        if client.download_file(file_id, local_path):
            print(f"     ✓ {len(local_path.read_bytes())} bytes")
        else:
            print(f"     ✗ Failed")
            return False

    # Download wiki/ subfolder
    wiki_folders = [f for f in files if f.get("name") == "wiki" and f.get("mimeType") == "application/vnd.google-apps.folder"]
    if wiki_folders:
        wiki_folder_id = wiki_folders[0]["id"]
        wiki_dir = LOCAL_PROJECT_DIR / "wiki"
        wiki_dir.mkdir(parents=True, exist_ok=True)

        # Download all wiki files recursively
        wiki_files = client.list_files(wiki_folder_id)
        for wiki_file in wiki_files:
            if wiki_file.get("mimeType") == "application/vnd.google-apps.folder":
                # Handle subdirectories (sources/, entities/, concepts/, synthesis/)
                subdir = wiki_dir / wiki_file["name"]
                subdir.mkdir(parents=True, exist_ok=True)

                subdir_files = client.list_files(wiki_file["id"])
                for subfile in subdir_files:
                    if subfile.get("mimeType") != "application/vnd.google-apps.folder":
                        local_path = subdir / subfile["name"]
                        print(f"   ⬇ wiki/{wiki_file['name']}/{subfile['name']}...")
                        if client.download_file(subfile["id"], local_path):
                            print(f"     ✓")
                        else:
                            print(f"     ✗")
            else:
                local_path = wiki_dir / wiki_file["name"]
                print(f"   ⬇ wiki/{wiki_file['name']}...")
                if client.download_file(wiki_file["id"], local_path):
                    print(f"     ✓")
                else:
                    print(f"     ✗")

    # Download raw/ subfolder
    raw_folders = [f for f in files if f.get("name") == "raw" and f.get("mimeType") == "application/vnd.google-apps.folder"]
    if raw_folders:
        raw_folder_id = raw_folders[0]["id"]
        raw_dir = LOCAL_PROJECT_DIR / "raw"
        raw_dir.mkdir(parents=True, exist_ok=True)

        raw_files = client.list_files(raw_folder_id)
        for raw_file in raw_files:
            if raw_file.get("mimeType") != "application/vnd.google-apps.folder":
                local_path = raw_dir / raw_file["name"]
                print(f"   ⬇ raw/{raw_file['name']}...")
                if client.download_file(raw_file["id"], local_path):
                    print(f"     ✓")
                else:
                    print(f"     ✗")

    print(f"✓ Project ready at {LOCAL_PROJECT_DIR}/")
    return True


def push_project(project_name: str) -> bool:
    """Upload project changes from /tmp/wiki-project/ to Drive."""
    client = get_client()
    if not client:
        return False

    folder_id = get_project_folder_id(project_name)
    if not folder_id:
        print(f"✗ Project '{project_name}' not found in projects.md")
        return False

    if not LOCAL_PROJECT_DIR.exists():
        print(f"✗ Local project directory not found: {LOCAL_PROJECT_DIR}")
        return False

    print(f"📤 Pushing {project_name} to Drive...")
    print(f"   Folder ID: {folder_id}")

    # Ensure wiki/ folder exists locally
    wiki_dir = LOCAL_PROJECT_DIR / "wiki"
    wiki_dir.mkdir(parents=True, exist_ok=True)

    # Get or create wiki/ folder on Drive
    wiki_folder_id = client.get_or_create_folder("wiki", folder_id)

    # Upload wiki files recursively
    wiki_dir = LOCAL_PROJECT_DIR / "wiki"
    if wiki_dir.exists():
        for file_path in wiki_dir.rglob("*"):
            if file_path.is_file():
                rel_path = file_path.relative_to(LOCAL_PROJECT_DIR)
                print(f"   ⬆ {rel_path}...")

                # Determine parent folder
                parent_folder_id = wiki_folder_id
                if file_path.parent.name != "wiki":
                    subdir_name = file_path.parent.name
                    parent_folder_id = client.get_or_create_folder(subdir_name, wiki_folder_id)

                if client.upload_file(file_path, parent_folder_id, file_path.name):
                    print(f"     ✓")
                else:
                    print(f"     ✗")
                    return False

    # Upload PROJECT.md if it exists
    project_md = LOCAL_PROJECT_DIR / "PROJECT.md"
    if project_md.exists():
        print(f"   ⬆ PROJECT.md...")
        if client.upload_file(project_md, folder_id):
            print(f"     ✓")
        else:
            print(f"     ✗")
            return False

    print(f"✓ Project pushed to Drive")
    return True


def main():
    """Command-line interface."""
    if len(sys.argv) < 3:
        print("Usage: python3 tools/sync_project.py <pull|push> <project-name>")
        print()
        print("Examples:")
        print("  python3 tools/sync_project.py pull CFMR-Lombardia")
        print("  python3 tools/sync_project.py push CFMR-Lombardia")
        sys.exit(1)

    command = sys.argv[1]
    project_name = sys.argv[2]

    if command == "pull":
        success = pull_project(project_name)
    elif command == "push":
        success = push_project(project_name)
    else:
        print(f"✗ Unknown command: {command}")
        sys.exit(1)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
