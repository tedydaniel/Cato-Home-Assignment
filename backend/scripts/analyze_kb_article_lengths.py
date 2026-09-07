"""Measure article sizes in a local Cato KB snapshot."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from statistics import median
from typing import Any

from scripts.paths import project_root

PROJECT_ROOT = project_root(__file__)
DEFAULT_SNAPSHOT_DIR = PROJECT_ROOT / "knowledge_base" / "snapshot"
WORD_PATTERN = re.compile(r"[\w]+(?:['’-][\w]+)*", re.UNICODE)


def count_words(markdown: str) -> int:
    """Count human-readable word-like units, independent of Markdown punctuation."""
    return len(WORD_PATTERN.findall(markdown))


def percentile(sorted_values: list[int], percentage: float) -> int:
    """Return the nearest-rank percentile for a non-empty sorted value list."""
    if not sorted_values:
        raise ValueError("Cannot calculate a percentile of an empty list.")
    index = max(0, min(len(sorted_values) - 1, round((len(sorted_values) - 1) * percentage)))
    return sorted_values[index]


def analyze_snapshot(snapshot_dir: Path) -> dict[str, Any]:
    manifest_path = snapshot_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    article_rows: list[dict[str, Any]] = []

    for entry in manifest["articles"]:
        if entry.get("status") == "failed":
            continue
        relative_path = Path(entry["path"])
        article_path = (snapshot_dir / relative_path).resolve()
        if snapshot_dir.resolve() not in article_path.parents:
            raise ValueError(f"Manifest article path escapes snapshot directory: {relative_path}")
        markdown = article_path.read_text(encoding="utf-8")
        article_rows.append(
            {
                "url": entry["url"],
                "path": relative_path.as_posix(),
                "word_count": count_words(markdown),
                "character_count": len(markdown),
            }
        )

    word_counts = sorted(article["word_count"] for article in article_rows)
    if not word_counts:
        raise ValueError("Snapshot manifest contains no downloaded articles.")

    summary = {
        "article_count": len(article_rows),
        "total_words": sum(word_counts),
        "minimum_words": word_counts[0],
        "maximum_words": word_counts[-1],
        "mean_words": round(sum(word_counts) / len(word_counts), 2),
        "median_words": median(word_counts),
        "p75_words": percentile(word_counts, 0.75),
        "p90_words": percentile(word_counts, 0.90),
        "p95_words": percentile(word_counts, 0.95),
        "p99_words": percentile(word_counts, 0.99),
        "articles_over_1000_words": sum(count > 1000 for count in word_counts),
        "articles_over_2000_words": sum(count > 2000 for count in word_counts),
    }
    return {"summary": summary, "articles": article_rows}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-dir", type=Path, default=DEFAULT_SNAPSHOT_DIR)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    report = analyze_snapshot(arguments.snapshot_dir)
    output_path = arguments.output or arguments.snapshot_dir / "article_word_counts.json"
    output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report["summary"], indent=2))
    print(f"Per-article report: {output_path.resolve()}")


if __name__ == "__main__":
    main()
