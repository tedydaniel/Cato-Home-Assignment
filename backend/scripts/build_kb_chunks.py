"""Build title-enriched, heading-aware chunks for KB retrieval and embedding."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

import tiktoken

from scripts.analyze_kb_article_lengths import DEFAULT_SNAPSHOT_DIR
from scripts.analyze_kb_sections import split_h2_sections
from scripts.download_llms_index import _atomic_write

EMBEDDING_MODEL = "text-embedding-3-small"
TARGET_TOKENS = 450
MAX_TOKENS = 600
OVERLAP_TOKENS = 75
FRONTMATTER_TITLE = re.compile(r'^title:\s*["\']?(.+?)["\']?\s*$', re.MULTILINE)
H1_TITLE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def article_title(markdown: str, fallback: str) -> str:
    """Read the canonical article title from frontmatter, then H1, then filename."""
    match = FRONTMATTER_TITLE.search(markdown)
    if match:
        return match.group(1)
    match = H1_TITLE.search(markdown)
    return match.group(1) if match else fallback


def section_body(section_markdown: str) -> str:
    """Remove the leading H2 because it is represented in structured metadata."""
    return section_markdown.split("\n", 1)[1] if "\n" in section_markdown else ""


def split_to_token_limit(
    text: str, *, encoding: tiktoken.Encoding, limit: int, overlap: int
) -> list[str]:
    """Split Markdown preferentially at paragraphs, with a token-slice fallback."""
    if len(encoding.encode(text)) <= limit:
        return [text]

    chunks: list[str] = []
    current = ""
    for paragraph in re.split(r"\n{2,}", text):
        candidate = paragraph if not current else f"{current}\n\n{paragraph}"
        if len(encoding.encode(candidate)) <= limit:
            current = candidate
            continue
        if current:
            chunks.append(current)
            overlap_text = encoding.decode(encoding.encode(current)[-overlap:])
            current = f"{overlap_text}\n\n{paragraph}"
        else:
            tokens = encoding.encode(paragraph)
            step = max(1, limit - overlap)
            for start in range(0, len(tokens), step):
                chunks.append(encoding.decode(tokens[start : start + limit]))
            current = ""

        if current and len(encoding.encode(current)) > limit:
            tokens = encoding.encode(current)
            chunks.append(encoding.decode(tokens[:limit]))
            current = encoding.decode(tokens[limit - overlap :])
    if current:
        chunks.append(current)
    return chunks


def build_chunks(
    snapshot_dir: Path,
    *,
    target_tokens: int = TARGET_TOKENS,
    max_tokens: int = MAX_TOKENS,
    overlap_tokens: int = OVERLAP_TOKENS,
) -> list[dict[str, Any]]:
    """Build deterministic chunks from each downloaded article in the manifest."""
    if not 0 < target_tokens <= max_tokens:
        raise ValueError("target_tokens must be positive and no greater than max_tokens")
    manifest = json.loads((snapshot_dir / "manifest.json").read_text(encoding="utf-8"))
    encoding = tiktoken.encoding_for_model(EMBEDDING_MODEL)
    chunks: list[dict[str, Any]] = []

    for article in manifest["articles"]:
        if article.get("status") == "failed":
            continue
        relative_path = Path(article["path"])
        path = (snapshot_dir / relative_path).resolve()
        if snapshot_dir.resolve() not in path.parents:
            raise ValueError(f"Manifest article path escapes snapshot directory: {relative_path}")
        markdown = path.read_text(encoding="utf-8")
        title = article_title(markdown, path.stem)
        sections = split_h2_sections(markdown) or [("Overview", f"## Overview\n{markdown}")]
        for section_index, (section_title, markdown_section) in enumerate(sections):
            prefix = f"Article title: {title}\nSection: {section_title}\n\n"
            content_limit = max_tokens - len(encoding.encode(prefix))
            content_target = min(target_tokens - len(encoding.encode(prefix)), content_limit)
            if content_target <= 0:
                raise ValueError(f"Title metadata is too large for {article['url']}")
            body = section_body(markdown_section).strip()
            if not body:
                continue
            body_chunks = split_to_token_limit(
                body,
                encoding=encoding,
                limit=content_target,
                overlap=overlap_tokens,
            )
            safe_body_chunks = [
                safe_chunk
                for body_chunk in body_chunks
                for safe_chunk in split_to_token_limit(
                    body_chunk,
                    encoding=encoding,
                    limit=content_target,
                    overlap=0,
                )
            ]
            for chunk_index, body_chunk in enumerate(safe_body_chunks):
                text = f"{prefix}{body_chunk}".strip()
                token_count = len(encoding.encode(text))
                if token_count > max_tokens:
                    raise ValueError(f"Chunk exceeds {max_tokens} tokens: {article['url']}")
                chunks.append(
                    {
                        "chunk_id": f"{path.stem}:s{section_index}:c{chunk_index}",
                        "text": text,
                        "token_count": token_count,
                        "article_title": title,
                        "article_url": article["url"],
                        "article_path": relative_path.as_posix(),
                        "article_sha256": article["sha256"],
                        "section_title": section_title,
                        "section_index": section_index,
                        "chunk_index": chunk_index,
                        "embedding_model": EMBEDDING_MODEL,
                        "target_tokens": content_target,
                    }
                )
    return chunks


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-dir", type=Path, default=DEFAULT_SNAPSHOT_DIR)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()

    chunks = build_chunks(arguments.snapshot_dir)
    output = arguments.output or arguments.snapshot_dir / "chunks.jsonl"
    payload = "".join(json.dumps(chunk, ensure_ascii=False) + "\n" for chunk in chunks)
    _atomic_write(output, payload.encode("utf-8"))
    print(f"Built {len(chunks)} chunks at {output.resolve()}")


if __name__ == "__main__":
    main()
