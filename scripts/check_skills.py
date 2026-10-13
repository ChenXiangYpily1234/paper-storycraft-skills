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
        # The Agent Skills specification requires name == parent directory.
        assert name.group(1) == path.parent.name, f"Invalid skill name in {path}: {name.group(1)}"
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)), path
        assert len(desc.group(1)) <= 1024 and desc.group(1).startswith("Use "), \
            f"Skill description needs a clear when-to-use trigger: {path}"
        for needle in ("## Execute this skill", "**Procedure**", "**Deliver:**", "**Evidence boundary:**"):
            assert needle in src, f"Skill missing actionable contract {needle}: {path}"
        names.append(name.group(1))
    assert len(names) == len(set(names)), "Duplicate Skill names"
    for p in ["README.md", "README_EN.md", "WORKFLOW.md"]:
        doc = (root / p).read_text(encoding="utf-8")
        assert "13" in doc and "13-section-revision/SKILL.md" in doc, p
    # Documentation-only regression gate; factual source verification still needs
    # manuscript-level review and cannot be guaranteed by this static check.
    guide = (root / "CITATION_GUIDE.md").read_text(encoding="utf-8")
    for term in ("benchmark", "model", "dataset", "bibliography", "citation"):
        assert term in guide.lower(), f"Citation guide missing required topic: {term}"
    for rel in [
        "PRINCIPLES.md", "WORKFLOW.md", "README.md", "README_EN.md",
        "02-introduction/SKILL.md", "03-related-work/SKILL.md",
        "04-method/SKILL.md", "05-experiment/SKILL.md",
        "09-consistency-validation/SKILL.md", "13-section-revision/SKILL.md",
    ]:
        assert "CITATION_GUIDE.md" in (root / rel).read_text(encoding="utf-8"), \
            f"Citation guide not referenced by {rel}"

    # Both language READMEs show reproducible, small animated examples.
    for lang, page_name in (("zh", "README.md"), ("en", "README_EN.md")):
        page = (root / page_name).read_text(encoding="utf-8")
        for topic in ("argument", "related-work"):
            image_path = f"assets/demo-{topic}-{lang}.gif"
            image = (root / image_path).read_bytes()
            assert image.startswith((b"GIF87a", b"GIF89a")) and image.endswith(b";"), image_path
            assert image.count(bytes((0x21, 0xF9, 0x04))) >= 3, image_path
            assert len(image) < 300_000, f"README animation too large: {image_path}"
            assert image_path in page, f"README missing animated example: {image_path}"
    # Shared editorial guidance is exported and linked from every Skill.
    editorial = (root / "EDITORIAL_PLAYBOOK.md").read_text(encoding="utf-8")
    assert "negative results" in editorial.lower() and "nature" in editorial.lower()
    assert "appendix" in editorial.lower() and "supplement" in editorial.lower()
    assert "prespecified" in editorial.lower(), "Evidence triage must protect primary outcomes"
    exported = (root / "scripts/export_skills.py").read_text(encoding="utf-8")
    assert '"EDITORIAL_PLAYBOOK.md"' in exported
    for path in files:
        body = path.read_text(encoding="utf-8")
        assert "### Decision and failure test" in body, f"Missing skill-specific failure gate: {path}"
        assert "EDITORIAL_PLAYBOOK.md" in body, f"Missing editorial routing: {path}"

    assert (root / "scripts/export_skills.py").exists(), "Missing portable Skill export"
    assert (root / "tests/skill-scenarios.md").exists(), "Missing behavior review scenarios"
    scenarios = (root / "tests/skill-scenarios.md").read_text(encoding="utf-8")
    for required in ("Scenario 11", "Scenario 12", "Scenario 13", "Scenario 16", "Scenario 17", "Scenario 18", "Scenario 19",
                     "PASS / FAIL / NOT CHECKED"):
        assert required in scenarios, f"Missing targeted behavior test: {required}"
    for file in ("README.md", "README_EN.md"):
        page = (root / file).read_text(encoding="utf-8")
        assert "scripts/export_skills.py" in page, f"Missing export instructions: {file}"
        assert "tests/skill-scenarios.md" in page, f"Missing scenario guidance: {file}"
        assert "EDITORIAL_PLAYBOOK.md" in page, f"Missing editorial entry point: {file}"
        prompt = "prompts/quick-start-zh.md" if file == "README.md" else "prompts/quick-start-en.md"
        assert prompt in page, f"Missing no-install prompt link: {file}"
    links = 0
    for p in [*root.glob("*.md"), *root.glob("[0-9][0-9]-*/SKILL.md"), *root.glob("prompts/*.md"), *root.glob("tests/*.md")]:
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
