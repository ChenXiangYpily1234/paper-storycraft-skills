#!/usr/bin/env python3
"""Export self-contained Paper StoryCraft Skill collection without changing agent settings.

Usage:
    python scripts/export_skills.py --output ./my-agent-skills

The output directory must not exist or must be empty. The script copies the
13 Skill folders plus shared Markdown guides so '../PRINCIPLES.md' and
cross-Skill links remain valid. No installed agent is modified.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys
import tempfile
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SHARED = ("PRINCIPLES.md", "CITATION_GUIDE.md", "STEM_GUIDE.md", "WORKFLOW.md")
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def validate_links(folder: Path) -> int:
    """Validate local Markdown links in the exported collection."""
    total = 0
    for file in folder.rglob("*.md"):
        for value in LINK.findall(file.read_text(encoding="utf-8")):
            path = unquote(value.split("#", 1)[0].strip())
            if not path or path.startswith(("http://", "https://", "mailto:", "/")):
                continue
            if not (file.parent / path).exists():
                raise ValueError(f"Unresolved link: {file.relative_to(folder)} -> {path}")
            total += 1
    return total


def export(output: Path) -> tuple[int, int]:
    folders = sorted(ROOT.glob("[0-9][0-9]-*/SKILL.md"))
    if len(folders) != 13:
        raise ValueError(f"Expected 13 Skills; found {len(folders)}")
    target = output.expanduser().resolve()
    if target == ROOT or ROOT in target.parents and any(
        target == f.parent or f.parent in target.parents for f in folders
    ):
        raise ValueError("Output cannot be inside an existing source Skill directory.")
    if target.exists() and any(target.iterdir()):
        raise FileExistsError(f"Target must be new or empty: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".storycraft-export-", dir=target.parent) as temp:
        stage = Path(temp) / "skills"
        stage.mkdir()
        for file in folders:
            shutil.copytree(file.parent, stage / file.parent.name)
        for file in SHARED:
            shutil.copy2(ROOT / file, stage / file)
        links = validate_links(stage)
        # Only delete an existing *empty* directory. Never overwrite user files.
        if target.exists():
            target.rmdir()
        shutil.move(str(stage), str(target))
    return len(folders), links


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path, help="New or empty directory for all 13 skills")
    args = parser.parse_args()
    try:
        count, links = export(args.output)
    except (ValueError, FileExistsError, OSError) as exc:
        parser.exit(2, f"Export failed: {exc}\n")
    print(f"PASS: exported {count} Skills and shared guides; verified {links} internal Markdown links")
    print(f"Output: {args.output.expanduser().resolve()}")
    print("Configure this directory in your agent manually; no installation was performed.")


if __name__ == "__main__":
    main()
