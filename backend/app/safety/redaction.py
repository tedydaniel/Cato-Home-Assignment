"""Deterministic redaction applied before customer content is persisted or traced."""

from __future__ import annotations

import re


_SECRET_PATTERNS = (
    re.compile(r"(?i)(api[_ -]?key\s*[:=]\s*)(\S+)"),
    re.compile(r"(?i)(password\s*[:=]\s*)(\S+)"),
    re.compile(r"(?i)((?:pre[- ]?shared key|psk|token)\s*[:=]\s*)(\S+)"),
)


def redact_secrets(text: str) -> str:
    """Replace credential values while retaining enough context to support safely."""
    for pattern in _SECRET_PATTERNS:
        text = pattern.sub(lambda match: f"{match.group(1)}[REDACTED]", text)
    return text
