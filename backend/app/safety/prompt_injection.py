"""Deterministic detection of clear attempts to override agent instructions."""

from __future__ import annotations

from dataclasses import dataclass
import re


_INJECTION_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("instruction_override", re.compile(r"\b(?:ignore|disregard)\s+(?:all\s+)?(?:previous|prior)\s+(?:instructions|rules|prompts)\b", re.IGNORECASE)),
    ("system_prompt_exfiltration", re.compile(r"\b(?:reveal|show|print|repeat)\s+(?:the\s+)?(?:system|developer)\s+prompt\b", re.IGNORECASE)),
    ("guardrail_bypass", re.compile(r"\b(?:bypass|disable|override)\s+(?:the\s+)?(?:safety|guardrails?|policy)\b", re.IGNORECASE)),
    ("jailbreak", re.compile(r"\b(?:jailbreak|developer\s+mode)\b", re.IGNORECASE)),
)


@dataclass(frozen=True)
class PromptInjectionAssessment:
    """Result used to keep untrusted instruction overrides out of the graph."""

    detected: bool
    signals: tuple[str, ...]


def detect_prompt_injection(text: str) -> PromptInjectionAssessment:
    """Detect explicit override or exfiltration attempts without an LLM decision."""

    signals = tuple(name for name, pattern in _INJECTION_PATTERNS if pattern.search(text))
    return PromptInjectionAssessment(detected=bool(signals), signals=signals)
