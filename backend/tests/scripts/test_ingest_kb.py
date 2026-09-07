import hashlib
import json
from pathlib import Path

import pytest

from scripts.ingest_kb import SnapshotIntegrityError, changed, load_snapshot_entries, vector_literal


def test_changed_only_when_the_remote_content_hash_differs() -> None:
    assert changed("new-hash", None)
    assert changed("new-hash", "old-hash")
    assert not changed("same-hash", "same-hash")


def test_vector_literal_uses_pgvector_syntax() -> None:
    assert vector_literal([0.25, -0.5]) == "[0.25,-0.5]"


def test_load_snapshot_entries_uses_the_pinned_manifest_without_network(tmp_path: Path) -> None:
    articles = tmp_path / "articles"
    articles.mkdir()
    contents = b"# Pinned article"
    (articles / "pinned.md").write_bytes(contents)
    (tmp_path / "manifest.json").write_text(json.dumps({"articles": [{
        "url": "https://knowledge.catonetworks.com/docs/pinned.md",
        "path": "articles/pinned.md", "sha256": hashlib.sha256(contents).hexdigest(),
    }]}), encoding="utf-8")

    entries = load_snapshot_entries(tmp_path)

    assert entries[0]["url"].endswith("pinned.md")


def test_load_snapshot_entries_rejects_an_article_changed_after_the_crawl(tmp_path: Path) -> None:
    articles = tmp_path / "articles"
    articles.mkdir()
    (articles / "changed.md").write_text("changed", encoding="utf-8")
    (tmp_path / "manifest.json").write_text(json.dumps({"articles": [{
        "url": "https://knowledge.catonetworks.com/docs/changed.md",
        "path": "articles/changed.md", "sha256": "not-the-real-hash",
    }]}), encoding="utf-8")

    with pytest.raises(SnapshotIntegrityError, match="hash does not match"):
        load_snapshot_entries(tmp_path)
