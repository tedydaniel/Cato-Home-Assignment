import hashlib
import json
from pathlib import Path

import tiktoken

from scripts.build_kb_chunks import article_title, build_chunks, split_to_token_limit


def test_article_title_prefers_frontmatter_then_h1_then_filename() -> None:
    assert article_title('---\ntitle: "Cato Guide"\n---\n# Other', "fallback") == "Cato Guide"
    assert article_title("# Cato Guide", "fallback") == "Cato Guide"
    assert article_title("No heading", "fallback") == "fallback"


def test_split_to_token_limit_preserves_the_token_limit() -> None:
    encoding = tiktoken.encoding_for_model("text-embedding-3-small")
    text = "\n\n".join(["word " * 30] * 8)

    chunks = split_to_token_limit(text, encoding=encoding, limit=50, overlap=10)

    assert len(chunks) > 1
    assert all(len(encoding.encode(chunk)) <= 50 for chunk in chunks)


def test_build_chunks_adds_title_metadata_and_splits_long_sections(tmp_path: Path) -> None:
    articles = tmp_path / "articles"
    articles.mkdir()
    markdown = "---\ntitle: Test Article\n---\n# Test Article\n## Troubleshooting\n" + ("network " * 200)
    (articles / "test.md").write_text(markdown, encoding="utf-8")
    (tmp_path / "manifest.json").write_text(
        json.dumps(
            {"articles": [{"url": "https://example.test/test.md", "path": "articles/test.md", "sha256": "abc"}]}
        ),
        encoding="utf-8",
    )

    chunks = build_chunks(tmp_path, target_tokens=50, max_tokens=70, overlap_tokens=10)

    assert len(chunks) > 1
    assert all(chunk["token_count"] <= 70 for chunk in chunks)
    assert all(chunk["article_title"] == "Test Article" for chunk in chunks)
    assert all("Article title: Test Article" in chunk["text"] for chunk in chunks)
    assert chunks[0]["article_sha256"] == "abc"


def test_build_chunks_uses_overview_for_articles_without_h2(tmp_path: Path) -> None:
    articles = tmp_path / "articles"
    articles.mkdir()
    (articles / "plain.md").write_text("# Plain Article\nUseful content.", encoding="utf-8")
    (tmp_path / "manifest.json").write_text(
        json.dumps({"articles": [{"url": "https://example.test/plain.md", "path": "articles/plain.md", "sha256": "abc"}]}),
        encoding="utf-8",
    )

    chunks = build_chunks(tmp_path)

    assert len(chunks) == 1
    assert chunks[0]["section_title"] == "Overview"
