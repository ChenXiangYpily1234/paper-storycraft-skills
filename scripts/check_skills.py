#!/usr/bin/env python3
"""Validate the published skill count, frontmatter and repository-local links."""
from pathlib import Path
import re
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]


def main():
    files = sorted(root.glob("[0-9][0-9]-*/SKILL.md"))
    assert len(files) == 13, f"Expected 13 skills, got {len(files)}"
    names = []
    for path in files:
        src = path.read_text(encoding="utf-8")
        assert src.startswith("---\n") and "\n---\n" in src[4:], path
        front = src.split("---", 2)[1]
        name = re.search(r"(?m)^name:\s*(\S.*)$", front)
        desc = re.search(r"(?m)^description:\s*(\S.*)$", front)
        assert name and desc, f"Missing Skill metadata: {path}"
        names.append(name.group(1))
    assert len(names) == len(set(names)), "Duplicate Skill names"
    for p in ["README.md", "README_EN.md", "WORKFLOW.md"]:
        doc = (root / p).read_text(encoding="utf-8")
        assert "13" in doc and "13-section-revision/SKILL.md" in doc, p
    links = 0
    for p in [*root.glob("*.md"), *root.glob("[0-9][0-9]-*/SKILL.md")]:
        doc = p.read_text(encoding="utf-8")
        for uri in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", doc):
            uri = uri.split("#", 1)[0].strip()
            if not uri or uri.startswith(("https://", "http://", "mailto:", "/")):
                continue
            assert (p.parent / unquote(uri)).exists(), f"Broken link in {p}: {uri}"
            links += 1
    print(f"PASS: {len(files)} skills, unique metadata, bilingual docs, {links} relative links")


if __name__ == "__main__":
    main()
