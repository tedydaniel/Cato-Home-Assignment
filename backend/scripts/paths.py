"""Resolve project paths consistently in local and container execution."""

from __future__ import annotations

import os
from pathlib import Path


def project_root(script_file: str | Path) -> Path:
    """Return the configured container root, or derive the local repository root."""
    configured_root = os.getenv("PROJECT_ROOT")
    if configured_root:
        return Path(configured_root)
    return Path(script_file).resolve().parents[2]
