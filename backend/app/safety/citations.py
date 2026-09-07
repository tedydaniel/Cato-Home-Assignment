"""Separate customer-safe citations from internal reviewer evidence."""

from collections.abc import Iterable
from typing import Any


def customer_safe_citations(citations: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    """Exclude internal policy references from customer-visible chat output.

    Policy evidence remains in durable graph state and reviewer traces.  It is
    intentionally not a public source the customer can open or inspect.
    """
    return [citation for citation in citations if not str(citation.get("source", "")).startswith("policy://")]
