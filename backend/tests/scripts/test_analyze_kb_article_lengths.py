import json
from pathlib import Path

import pytest

from scripts.analyze_kb_article_lengths import analyze_snapshot, count_words, percentile


def test_count_words_ignores_markdown_punctuation() -> None:
    assert count_words("# Cato's **IPsec** guide — step-by-step.") == 4


def test_percentile_uses_nearest_rank_and_rejects_empty_values() -> None:
    assert percentile([10, 20, 30, 40], 0.75) == 30
    with pytest.raises(ValueError, match="empty"):
        percentile([], 0.5)


def test_analyze_snapshot_returns_per_article_and_summary(tmp_path: Path) -> None:
    articles_dir = tmp_path / "articles"
    articles_dir.mkdir()
    (articles_dir / "one.md").write_text("One two three.", encoding="utf-8")
    (articles_dir / "two.md").write_text("One two.", encoding="utf-8")
    (tmp_path / "manifest.json").write_text(
        json.dumps(
            {
                "articles": [
                    {"url": "https://example.test/one", "path": "articles/one.md"},
                    {"url": "https://example.test/two", "path": "articles/two.md"},
                    {"url": "https://example.test/failed", "status": "failed"},
                ]
            }
        ),
        encoding="utf-8",
    )

    report = analyze_snapshot(tmp_path)

    assert report["summary"]["article_count"] == 2
    assert report["summary"]["total_words"] == 5
    assert report["articles"][0]["word_count"] == 3


def test_analyze_snapshot_rejects_a_manifest_path_outside_the_snapshot(tmp_path: Path) -> None:
    (tmp_path / "manifest.json").write_text(
        json.dumps({"articles": [{"url": "https://example.test", "path": "../outside.md"}]}),
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="escapes"):
        analyze_snapshot(tmp_path)
