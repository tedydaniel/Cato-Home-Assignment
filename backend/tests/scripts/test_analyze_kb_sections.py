import json
from pathlib import Path

from scripts.analyze_kb_sections import analyze_sections, split_h2_sections


def test_split_h2_sections_keeps_child_content_and_ignores_code_fences() -> None:
    markdown = """# Article
Preamble.
## First section
First content.
### Child heading
Child content.
```markdown
## Not a real section
```
## Second section ##
Second content.
"""

    sections = split_h2_sections(markdown)

    assert [title for title, _ in sections] == ["First section", "Second section"]
    assert "### Child heading" in sections[0][1]
    assert "## Not a real section" in sections[0][1]


def test_analyze_sections_returns_distribution(tmp_path: Path) -> None:
    articles_dir = tmp_path / "articles"
    articles_dir.mkdir()
    (articles_dir / "one.md").write_text(
        "# One\n## First\nOne two three.\n## Second\nOne two.", encoding="utf-8"
    )
    (articles_dir / "two.md").write_text("# Two\nNo H2.", encoding="utf-8")
    (tmp_path / "manifest.json").write_text(
        json.dumps(
            {
                "articles": [
                    {"url": "https://example.test/one", "path": "articles/one.md"},
                    {"url": "https://example.test/two", "path": "articles/two.md"},
                ]
            }
        ),
        encoding="utf-8",
    )

    report = analyze_sections(tmp_path)

    assert report["summary"]["section_count"] == 2
    assert report["summary"]["articles_without_h2"] == 1
    assert [section["word_count"] for section in report["sections"]] == [4, 3]
