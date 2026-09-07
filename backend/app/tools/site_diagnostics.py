"""Customer-scoped site telemetry tools backed by the supplied CMA snapshot."""

from __future__ import annotations

import csv
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Literal

from langchain.tools import ToolRuntime, tool
from pydantic import BaseModel, Field

from app.tools.diagnostics import _trusted_customer_id
from app.config import get_settings


class SiteInput(BaseModel):
    site_id: str = Field(pattern=r"^S-\d{4}-\d{2}$")


class EventsInput(SiteInput):
    event_type: str | None = Field(default=None, max_length=100)


def _site_is_authorized(site_id: str, runtime: ToolRuntime) -> bool:
    customer_id = _trusted_customer_id(runtime)
    if not customer_id:
        return False
    try:
        sites = json.loads((get_settings().data_path / "telemetry" / "sites.json").read_text(encoding="utf-8"))["sites"]
    except (OSError, json.JSONDecodeError, KeyError):
        return False
    return any(site.get("site_id") == site_id and site.get("customer_id") == customer_id for site in sites)


def _error(tool_name: str, code: Literal["unauthorized", "not_found", "invalid_telemetry"]) -> dict[str, str]:
    messages = {
        "unauthorized": "Site telemetry is not available for the active customer.",
        "not_found": "No telemetry is available for this site.",
        "invalid_telemetry": "Site telemetry is temporarily unavailable due to invalid data.",
    }
    return {"status": "error", "tool_name": tool_name, "code": code, "message": messages[code]}


def _load_json(tool_name: str, folder: str, site_id: str, runtime: ToolRuntime) -> dict[str, Any]:
    if not _site_is_authorized(site_id, runtime):
        return _error(tool_name, "unauthorized")
    try:
        payload = json.loads((get_settings().data_path / "telemetry" / folder / f"{site_id}.json").read_text(encoding="utf-8"))
    except FileNotFoundError:
        return _error(tool_name, "not_found")
    except (OSError, json.JSONDecodeError):
        return _error(tool_name, "invalid_telemetry")
    if payload.get("site_id") != site_id:
        return _error(tool_name, "invalid_telemetry")
    return payload


@tool(args_schema=SiteInput)
def get_site_status(site_id: str, runtime: ToolRuntime) -> dict[str, Any]:
    """Return CMA site status and metadata for an authorized customer site."""
    if not _site_is_authorized(site_id, runtime):
        return _error("get_site_status", "unauthorized")
    try:
        sites = json.loads((get_settings().data_path / "telemetry" / "sites.json").read_text(encoding="utf-8"))["sites"]
        site = next(item for item in sites if item.get("site_id") == site_id)
    except (OSError, json.JSONDecodeError, KeyError, StopIteration):
        return _error("get_site_status", "not_found")
    return {"status": "ok", "tool_name": "get_site_status", "source": "telemetry:site_status", "query": {"site_id": site_id}, "facts": site}


@tool(args_schema=SiteInput)
def get_bgp_status(site_id: str, runtime: ToolRuntime) -> dict[str, Any]:
    """Return BGP neighbor state, route limits, flaps, and errors for an authorized site."""
    payload = _load_json("get_bgp_status", "bgp_status", site_id, runtime)
    if payload.get("status") == "error":
        return payload
    return {"status": "ok", "tool_name": "get_bgp_status", "source": "telemetry:bgp_status", "query": {"site_id": site_id}, "observed_at": payload.get("queried_at"), "facts": {"neighbors": payload["neighbors"]}}


@tool(args_schema=SiteInput)
def get_ipsec_status(site_id: str, runtime: ToolRuntime) -> dict[str, Any]:
    """Return IKE/IPsec tunnel status and peer-proposal evidence for an authorized site."""
    payload = _load_json("get_ipsec_status", "ipsec_status", site_id, runtime)
    if payload.get("status") == "error":
        return payload
    return {"status": "ok", "tool_name": "get_ipsec_status", "source": "telemetry:ipsec_status", "query": {"site_id": site_id}, "observed_at": payload.get("queried_at"), "facts": payload}


@tool(args_schema=SiteInput)
def get_link_quality(site_id: str, runtime: ToolRuntime) -> dict[str, Any]:
    """Summarize 24-hour packet loss, latency, and jitter for an authorized site."""
    if not _site_is_authorized(site_id, runtime):
        return _error("get_link_quality", "unauthorized")
    path = get_settings().data_path / "telemetry" / "link_quality" / f"{site_id}.csv"
    try:
        rows = list(csv.DictReader(path.open(encoding="utf-8", newline="")))
    except FileNotFoundError:
        return _error("get_link_quality", "not_found")
    except OSError:
        return _error("get_link_quality", "invalid_telemetry")
    if not rows:
        return _error("get_link_quality", "invalid_telemetry")
    by_link: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_link[row["link"]].append(row)
    try:
        summary = [{"link": link, "max_packet_loss_pct": max(float(row["packet_loss_pct"]) for row in values), "max_latency_ms": max(float(row["latency_ms"]) for row in values), "max_jitter_ms": max(float(row["jitter_ms"]) for row in values)} for link, values in by_link.items()]
    except (KeyError, ValueError):
        return _error("get_link_quality", "invalid_telemetry")
    return {"status": "ok", "tool_name": "get_link_quality", "source": "telemetry:link_quality", "query": {"site_id": site_id}, "facts": {"links": summary}}


@tool(args_schema=EventsInput)
def get_events(site_id: str, runtime: ToolRuntime, event_type: str | None = None) -> dict[str, Any]:
    """Return recent CMA events, optionally filtered by event type, for an authorized site."""
    if not _site_is_authorized(site_id, runtime):
        return _error("get_events", "unauthorized")
    path = get_settings().data_path / "telemetry" / "events" / f"{site_id}.jsonl"
    try:
        events = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    except FileNotFoundError:
        return _error("get_events", "not_found")
    except (OSError, json.JSONDecodeError):
        return _error("get_events", "invalid_telemetry")
    events = [event for event in events if event.get("site_id") == site_id and (event_type is None or event.get("event_type") == event_type)]
    return {"status": "ok", "tool_name": "get_events", "source": "telemetry:events", "query": {"site_id": site_id, "event_type": event_type}, "facts": {"events": events[-10:]}}
