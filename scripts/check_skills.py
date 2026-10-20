#!/usr/bin/env python3
"""Validate the published skill count, frontmatter and repository-local links."""
from pathlib import Path
from PIL import Image

from export_skills import SHARED
from validation import local_link_destinations, read_skill_metadata, require, validate_links

root = Path(__file__).resolve().parents[1]
MAX_README_GIF_BYTES = 900_000


def main():
    files = sorted(root.glob("[0-9][0-9]-*/SKILL.md"))
    require(len(files) == 13, f"Expected 13 skills, got {len(files)}")
    names = []
    for path in files:
        src = path.read_text(encoding="utf-8")
        metadata = read_skill_metadata(path)
        for needle in ("## Execute this skill", "**Procedure**", "**Deliver:**", "**Evidence boundary:**"):
            require(needle in src, f"Skill missing actionable contract {needle}: {path}")
        names.append(metadata["name"])
    require(len(names) == len(set(names)), "Duplicate Skill names")
    for p in ["README.md", "README_EN.md", "WORKFLOW.md"]:
        doc = (root / p).read_text(encoding="utf-8")
        require("13" in doc and "13-section-revision/SKILL.md" in doc, p)
    # Documentation-only regression gate; factual source verification still needs
    # manuscript-level review and cannot be guaranteed by this static check.
    guide = (root / "CITATION_GUIDE.md").read_text(encoding="utf-8")
    for term in ("benchmark", "model", "dataset", "bibliography", "citation"):
        require(term in guide.lower(), f"Citation guide missing required topic: {term}")
    for rel in [
        "PRINCIPLES.md", "WORKFLOW.md", "README.md", "README_EN.md",
        "02-introduction/SKILL.md", "03-related-work/SKILL.md",
        "04-method/SKILL.md", "05-experiment/SKILL.md",
        "09-consistency-validation/SKILL.md", "13-section-revision/SKILL.md",
    ]:
        require("CITATION_GUIDE.md" in (root / rel).read_text(encoding="utf-8"),
                f"Citation guide not referenced by {rel}")

    # Both language READMEs show three small animations with static alternatives.
    for lang, page_name in (("zh", "README.md"), ("en", "README_EN.md")):
        page = (root / page_name).read_text(encoding="utf-8")
        destinations = set(local_link_destinations(page))
        for topic in ("argument", "related-work", "experiments"):
            image_path = f"assets/demo-{topic}-{lang}.gif"
            require((root / image_path).stat().st_size < MAX_README_GIF_BYTES,
                    f"README animation too large: {image_path}")
            require(image_path in destinations, f"README missing animated example: {image_path}")
            with Image.open(root / image_path) as image:
                require(image.format == "GIF" and image.n_frames >= 3,
                        f"Expected animated GIF: {image_path}")
                size = image.size
                for frame in range(image.n_frames):
                    image.seek(frame)
                    image.load()
            static_path = f"assets/demo-{topic}-{lang}.png"
            require(static_path in destinations, f"README missing static example: {static_path}")
            with Image.open(root / static_path) as image:
                require(image.format == "PNG", f"Expected PNG: {static_path}")
                image.load()
                require(image.size == size, f"GIF/PNG dimensions differ: {image_path}")
    # Shared editorial guidance is exported and linked from every Skill.
    editorial = (root / "EDITORIAL_PLAYBOOK.md").read_text(encoding="utf-8")
    require("negative results" in editorial.lower() and "nature" in editorial.lower(),
            "Editorial guide missing framing or negative-result guidance")
    require("appendix" in editorial.lower() and "supplement" in editorial.lower(),
            "Editorial guide missing supplementary evidence guidance")
    require("prespecified" in editorial.lower(), "Evidence triage must protect primary outcomes")
    require({"EDITORIAL_PLAYBOOK.md", "LICENSE"} <= set(SHARED), "Export missing shared guide or license")
    for path in files:
        body = path.read_text(encoding="utf-8")
        require("### Decision and failure test" in body, f"Missing skill-specific failure gate: {path}")
        require("EDITORIAL_PLAYBOOK.md" in body, f"Missing editorial routing: {path}")

    require((root / "scripts/export_skills.py").exists(), "Missing portable Skill export")
    require((root / "tests/skill-scenarios.md").exists(), "Missing behavior review scenarios")
    scenarios = (root / "tests/skill-scenarios.md").read_text(encoding="utf-8")
    for required in ("Scenario 11", "Scenario 12", "Scenario 13", "Scenario 16", "Scenario 17", "Scenario 18", "Scenario 19",
                     "PASS / FAIL / NOT CHECKED"):
        require(required in scenarios, f"Missing targeted behavior test: {required}")
    for file in ("README.md", "README_EN.md"):
        page = (root / file).read_text(encoding="utf-8")
        require("scripts/export_skills.py" in page, f"Missing export instructions: {file}")
        require("tests/skill-scenarios.md" in page, f"Missing scenario guidance: {file}")
        require("EDITORIAL_PLAYBOOK.md" in page, f"Missing editorial entry point: {file}")
        prompt = "prompts/quick-start-zh.md" if file == "README.md" else "prompts/quick-start-en.md"
        require(prompt in page, f"Missing no-install prompt link: {file}")
    documents = [*root.glob("*.md"), *root.glob("prompts/**/*.md"), *root.glob("tests/**/*.md")]
    for path in files:
        documents.extend(path.parent.rglob("*.md"))
    links = validate_links(root, documents)
    print(f"PASS: {len(files)} skills, strict metadata, 6 GIF/PNG pairs, {links} local links")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(f"FAIL: {exc}") from exc
