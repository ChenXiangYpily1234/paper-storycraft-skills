"""Shared checks for Skill metadata and local documentation dependencies.

Links use CommonMark parsing, plus href/src from HTML a/img tags. Remote URLs
and heading fragments are not verified; this is not a complete GitHub renderer.
"""
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

try:
    from markdown_it import MarkdownIt
    import yaml
except ImportError as exc:
    raise SystemExit("Install validation dependencies: python -m pip install -r requirements-dev.txt") from exc


def require(condition, message):
    """Keep validation active even when Python is run with -O."""
    if not condition:
        raise ValueError(str(message))


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject ambiguous duplicate mapping keys instead of silently replacing them."""


def _unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str) or key in result:
            raise yaml.constructor.ConstructorError(
                "while reading a mapping", node.start_mark,
                f"Expected a unique string key; got {key!r}", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _unique_mapping)


def read_skill_metadata(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").splitlines()
    require(lines and lines[0] == "---", f"Missing YAML frontmatter: {path}")
    try:
        end = lines.index("---", 1)
        metadata = yaml.load("\n".join(lines[1:end]), Loader=UniqueKeyLoader)
    except (ValueError, yaml.YAMLError) as exc:
        raise ValueError(f"Invalid YAML frontmatter in {path}: {exc}") from exc
    require(isinstance(metadata, dict), f"Frontmatter must be a mapping: {path}")
    name, description = metadata.get("name"), metadata.get("description")
    require(isinstance(name, str) and name == path.parent.name,
            f"Skill name must match its directory: {path}")
    require(len(name) <= 64 and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name),
            f"Invalid Skill name: {path}")
    require(isinstance(description, str) and 0 < len(description) <= 1024
            and description.startswith("Use "), f"Invalid Skill description: {path}")
    return metadata


class _HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []

    def handle_starttag(self, tag, attrs):
        key = {"a": "href", "img": "src"}.get(tag)
        if key:
            value = dict(attrs).get(key)
            if value:
                self.links.append(value)


def local_link_destinations(source: str):
    """Yield rendered links/images, including reference links but excluding code."""
    def walk(tokens):
        for token in tokens:
            if token.type in ("link_open", "image"):
                yield token.attrGet("href" if token.type == "link_open" else "src")
            elif token.type in ("html_inline", "html_block"):
                parser = _HTMLLinks()
                parser.feed(token.content)
                yield from parser.links
            if token.children:
                yield from walk(token.children)
    yield from walk(MarkdownIt("commonmark").parse(source))


def validate_links(folder: Path, files=None) -> int:
    """Require local dependencies to exist within the collection, after resolving symlinks."""
    folder = folder.resolve()
    total = 0
    for file in sorted(files if files is not None else folder.rglob("*.md")):
        for value in local_link_destinations(file.read_text(encoding="utf-8")):
            parsed = urlsplit(value)
            require(parsed.scheme != "file", f"Nonportable file URL: {file} -> {value}")
            if parsed.scheme or parsed.netloc:
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            target = (file.parent / path).resolve()
            require(not Path(path).is_absolute() and target.is_relative_to(folder),
                    f"Link leaves collection: {file.relative_to(folder)} -> {value}")
            require(target.exists(), f"Unresolved link: {file.relative_to(folder)} -> {value}")
            total += 1
    return total
