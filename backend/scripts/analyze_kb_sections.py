"""Measure word counts of level-two Markdown sections in a local KB snapshot."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from statistics import median
from typing import Any

from scripts.analyze_kb_article_lengths import (
    DEFAULT_SNAPSHOT_DIR,
    count_words,
    percentile,
)

H2_PATTERN = re.compile(r"^##(?!#)\s+(.+?)\s*#*\s*$")


def split_h2_sections(markdown: str) -> list[tuple[str, str]]:
    """Return level-two sections, retaining child headings and ignoring fenced code."""
    sections: list[tuple[str, str]] = []
    title: str | None = None
    content: list[str] = []
    in_fence = False

    for line in markdown.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence

        match = None if in_fence else H2_PATTERN.match(line)
        if match:
            if title is not None:
                sections.append((title, "\n".join(content)))
            title = match.group(1)
            content = [line]
        elif title is not None:
            content.append(line)

    if title is not None:
        sections.append((title, "\n".join(content)))
    return sections


def analyze_sections(snapshot_dir: Path) -> dict[str, Any]:
    manifest = json.loads((snapshot_dir / "manifest.json").read_text(encoding="utf-8"))
    sections: list[dict[str, Any]] = []
    articles_without_h2 = 0

    for entry in manifest["articles"]:
        if entry.get("status") == "failed":
            continue
        relative_path = Path(entry["path"])
        article_path = (snapshot_dir / relative_path).resolve()
        if snapshot_dir.resolve() not in article_path.parents:
            raise ValueError(f"Manifest article path escapes snapshot directory: {relative_path}")
        article_sections = split_h2_sections(article_path.read_text(encoding="utf-8"))
        if not article_sections:
            articles_without_h2 += 1
        for section_title, section_markdown in article_sections:
            sections.append(
                {
                    "url": entry["url"],
                    "path": relative_path.as_posix(),
                    "section_title": section_title,
                    "word_count": count_words(section_markdown),
                    "character_count": len(section_markdown),
                }
            )

    word_counts = sorted(section["word_count"] for section in sections)
    if not word_counts:
        raise ValueError("Snapshot contains no level-two Markdown sections.")
    summary = {
        "section_count": len(sections),
        "articles_without_h2": articles_without_h2,
        "total_words": sum(word_counts),
        "minimum_words": word_counts[0],
        "maximum_words": word_counts[-1],
        "mean_words": round(sum(word_counts) / len(word_counts), 2),
        "median_words": median(word_counts),
        "p75_words": percentile(word_counts, 0.75),
        "p90_words": percentile(word_counts, 0.90),
        "p95_words": percentile(word_counts, 0.95),
        "p99_words": percentile(word_counts, 0.99),
        "sections_over_700_words": sum(count > 700 for count in word_counts),
        "sections_over_1200_words": sum(count > 1200 for count in word_counts),
    }
    return {"summary": summary, "sections": sections}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-dir", type=Path, default=DEFAULT_SNAPSHOT_DIR)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    report = analyze_sections(arguments.snapshot_dir)
    output_path = arguments.output or arguments.snapshot_dir / "section_word_counts.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(f"Per-section report: {output_path.resolve()}")


if __name__ == "__main__":
    main()
