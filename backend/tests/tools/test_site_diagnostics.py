import json
from types import SimpleNamespace
from typing import Any, cast

from app.tools import site_diagnostics


def test_site_status_returns_authorized_site_metadata(monkeypatch) -> None:
    runtime = type("Runtime", (), {"context": {"customer_id": "ACC-1007"}})()
    result = site_diagnostics.get_site_status.func(site_id="S-1007-01", runtime=runtime)

    assert result["status"] == "ok"
    assert result["source"] == "telemetry:site_status"


def _runtime(customer_id: str | None) -> Any:
    return cast(Any, SimpleNamespace(context={} if customer_id is None else {"customer_id": customer_id}))


def _prepare_telemetry(tmp_path, monkeypatch) -> None:
    telemetry = tmp_path / "telemetry"
    (telemetry / "bgp_status").mkdir(parents=True)
    (telemetry / "link_quality").mkdir()
    (telemetry / "sites.json").write_text(json.dumps({"sites": [{"site_id": "S-1007-01", "customer_id": "ACC-1007"}]}), encoding="utf-8")
    (telemetry / "bgp_status" / "S-1007-01.json").write_text(json.dumps({"site_id": "S-1007-01", "queried_at": "2026-08-28T17:00:00Z", "neighbors": [{"routes_count": 1024, "routes_limit": 1024}]}), encoding="utf-8")
    (telemetry / "link_quality" / "S-1007-01.csv").write_text("ts,link,packet_loss_pct,latency_ms,jitter_ms\n2026-08-28T17:00:00Z,WAN1,2.5,44.0,8.0\n", encoding="utf-8")
    monkeypatch.setattr(site_diagnostics, "get_settings", lambda: SimpleNamespace(data_path=tmp_path))


def test_bgp_tool_returns_citable_authorized_evidence(tmp_path, monkeypatch) -> None:
    _prepare_telemetry(tmp_path, monkeypatch)
    assert site_diagnostics.get_bgp_status.func is not None

    result = site_diagnostics.get_bgp_status.func(site_id="S-1007-01", runtime=_runtime("ACC-1007"))

    assert result["status"] == "ok"
    assert result["source"] == "telemetry:bgp_status"
    assert result["facts"]["neighbors"][0]["routes_count"] == 1024


def test_site_tools_deny_cross_customer_access(tmp_path, monkeypatch) -> None:
    _prepare_telemetry(tmp_path, monkeypatch)
    assert site_diagnostics.get_link_quality.func is not None

    result = site_diagnostics.get_link_quality.func(site_id="S-1007-01", runtime=_runtime("ACC-9999"))

    assert result["status"] == "error"
    assert result["code"] == "unauthorized"


def test_link_quality_tool_summarizes_metrics(tmp_path, monkeypatch) -> None:
    _prepare_telemetry(tmp_path, monkeypatch)
    assert site_diagnostics.get_link_quality.func is not None

    result = site_diagnostics.get_link_quality.func(site_id="S-1007-01", runtime=_runtime("ACC-1007"))

    assert result["facts"]["links"] == [{"link": "WAN1", "max_packet_loss_pct": 2.5, "max_latency_ms": 44.0, "max_jitter_ms": 8.0}]
