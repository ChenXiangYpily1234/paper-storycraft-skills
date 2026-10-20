"""Regression checks for rejected invalid inputs and portable, non-destructive exports."""
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import export_skills
from validation import read_skill_metadata, validate_links


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "collection"
        self.root.mkdir()

    def test_metadata_parses_yaml_and_rejects_ambiguous_or_invalid_fields(self):
        skill = self.root / "01-example" / "SKILL.md"
        skill.parent.mkdir()
        valid = 'name: 01-example\ndescription: "Use when checking a claim: keep its evidence."\n'
        skill.write_text(f"---\n{valid}---\n# Example\n", encoding="utf-8")
        self.assertEqual(read_skill_metadata(skill)["name"], "01-example")
        invalid = (
            valid + "name: another-name\n",
            "name: 01-example\ndescription: Use invalid: YAML\n",
            "name: 01-example\ndescription: [Use, a, list]\n",
            "name: another-name\ndescription: Use valid text.\n",
        )
        for front in invalid:
            with self.subTest(front=front):
                skill.write_text(f"---\n{front}---\n# Example\n", encoding="utf-8")
                with self.assertRaises(ValueError):
                    read_skill_metadata(skill)

    def test_missing_images_and_reference_links_fail(self):
        document = self.root / "guide.md"
        for source in (
            "![Diagram](missing.png)",
            "[Source][ref]\n\n[ref]: missing.md\n",
            '<img src="missing.png" alt="Diagram">',
        ):
            with self.subTest(source=source):
                document.write_text(source, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Unresolved link"):
                    validate_links(self.root)

    def test_valid_link_syntax_and_code_examples(self):
        (self.root / "file (copy).md").write_text("# Target\n", encoding="utf-8")
        (self.root / "diagram.png").write_bytes(b"placeholder; link existence only")
        (self.root / "guide.md").write_text(
            '[Text](<file (copy).md> "Optional title")\n'
            '![Diagram][image]\n\n[image]: diagram.png "Title"\n'
            '`[Inline code](does-not-exist.md)`\n\n'
            '~~~markdown\n[Code sample](does-not-exist.md)\n~~~\n'
            '[Web](https://example.org)\n[Heading](#target)\n', encoding="utf-8")
        self.assertEqual(validate_links(self.root), 2)

    def test_existing_outside_dependency_is_rejected(self):
        outside = self.root.parent / "outside.md"
        outside.write_text("# Outside\n", encoding="utf-8")
        for destination in ("../outside.md", str(outside)):
            with self.subTest(destination=destination):
                (self.root / "guide.md").write_text(f"[External]({destination})", encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "Link leaves collection"):
                    validate_links(self.root)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.source = self.base / "source"
        self.source.mkdir()
        for skill in ROOT.glob("[0-9][0-9]-*/SKILL.md"):
            shutil.copytree(skill.parent, self.source / skill.parent.name,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        for name in export_skills.SHARED:
            shutil.copy2(ROOT / name, self.source / name)
        self.patcher = patch.object(export_skills, "ROOT", self.source)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def test_export_retains_license_and_links_after_relocation(self):
        output = self.base / "output"
        self.assertEqual(export_skills.export(output)[0], 13)
        relocated = self.base / "another-parent" / "skills"
        relocated.parent.mkdir()
        shutil.move(str(output), str(relocated))
        shutil.rmtree(self.source)
        self.assertEqual((relocated / "LICENSE").read_bytes(), (ROOT / "LICENSE").read_bytes())
        self.assertGreater(validate_links(relocated), 0)
        self.assertTrue((relocated / "11-research-plot/scripts/plot_ordered_series.py").is_file())

    def test_nonempty_target_and_source_directory_are_preserved(self):
        output = self.base / "occupied"
        output.mkdir()
        marker = output / "keep.txt"
        marker.write_bytes(b"keep exactly")
        with self.assertRaises(FileExistsError):
            export_skills.export(output)
        self.assertEqual(marker.read_bytes(), b"keep exactly")
        with self.assertRaises(ValueError):
            export_skills.export(self.source / "01-abstract" / "nested-export")
        self.assertFalse((self.source / "01-abstract/nested-export").exists())

    def test_invalid_staged_dependency_does_not_publish_a_partial_export(self):
        # This path previously resolved inside the temporary staging parent, then
        # broke after the stage was moved to its final destination.
        (self.base / "outside.md").write_text("# External\n", encoding="utf-8")
        skill = self.source / "01-abstract/SKILL.md"
        with skill.open("a", encoding="utf-8") as stream:
            stream.write("\n[External](../../../outside.md)\n")
        output = self.base / "output"
        with self.assertRaisesRegex(ValueError, "Link leaves collection"):
            export_skills.export(output)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
