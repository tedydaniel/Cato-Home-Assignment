import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import pytest

from app.tools import diagnostics


def test_client_diagnostics_accepts_records_without_optional_provisioning() -> None:
    result = diagnostics.ClientDiagnostics.model_validate({"customer_id": "ACC-1", "os": "Windows", "client_version": "5", "last_connect_attempt": "2026-08-28T17:00:00Z", "last_error": None, "network": {"ssid": "wifi", "captive_portal_detected": False, "udp_443_reachable": True, "tcp_443_reachable": True}, "user_email": "user@example.com", "queried_at": "2026-08-28T17:00:00Z"})

    assert result.provisioning is None
    assert result.last_error is None


def _telemetry_payload(customer_id: str = "ACC-1006") -> dict[str, Any]:
    return {
        "customer_id": customer_id,
        "os": "macOS 15.1",
        "client_version": "5.10.0",
        "last_connect_attempt": "2026-08-28T16:20:00Z",
        "last_error": "AUTH_FAILED (401)",
        "provisioning": {
            "scim_status": "not provisioned",
            "last_scim_sync": "2026-08-27T15:00:00Z",
            "last_scim_result": "Failed: Internal Server Error",
        },
        "network": {
            "ssid": "corp",
            "captive_portal_detected": False,
            "udp_443_reachable": True,
            "tcp_443_reachable": True,
        },
        "user_email": "hana.iyer@verdantfoods.com",
        "queried_at": "2026-08-28T17:00:00Z",
    }


@pytest.fixture
def telemetry_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    clients_dir = tmp_path / "telemetry" / "clients"
    clients_dir.mkdir(parents=True)
    monkeypatch.setattr(
        diagnostics,
        "get_settings",
        lambda: SimpleNamespace(data_path=tmp_path),
    )
    return clients_dir


def _runtime(customer_id: str | None) -> Any:
    context = {} if customer_id is None else {"customer_id": customer_id}
    return cast(Any, SimpleNamespace(context=context))


def _invoke_tool(user_email: str, customer_id: str | None) -> dict[str, Any]:
    assert diagnostics.get_client_diagnostics.func is not None
    return diagnostics.get_client_diagnostics.func(
        user_email=user_email,
        runtime=_runtime(customer_id),
    )


def test_schema_exposes_only_user_email_to_the_model() -> None:
    assert set(diagnostics.get_client_diagnostics.args_schema.model_fields) == {"user_email"}


def test_returns_citable_evidence_for_the_authorized_customer(telemetry_dir: Path) -> None:
    (telemetry_dir / "hana.iyer@verdantfoods.com.json").write_text(
        json.dumps(_telemetry_payload()), encoding="utf-8"
    )

    result = _invoke_tool("hana.iyer@verdantfoods.com", "ACC-1006")

    assert result["status"] == "ok"
    assert result["tool_name"] == "get_client_diagnostics"
    assert result["source"] == "telemetry:client_diagnostics"
    assert result["facts"]["last_error"] == "AUTH_FAILED (401)"


def test_returns_not_found_when_diagnostics_do_not_exist(telemetry_dir: Path) -> None:
    result = _invoke_tool("missing@example.com", "ACC-1006")

    assert result == {
        "status": "error",
        "tool_name": "get_client_diagnostics",
        "code": "not_found",
        "message": "No Cato Client diagnostics are available for that user.",
    }


def test_returns_invalid_telemetry_for_a_malformed_file(telemetry_dir: Path) -> None:
    (telemetry_dir / "hana.iyer@verdantfoods.com.json").write_text("{}", encoding="utf-8")

    result = _invoke_tool("hana.iyer@verdantfoods.com", "ACC-1006")

    assert result["status"] == "error"
    assert result["code"] == "invalid_telemetry"


def test_denies_a_call_without_trusted_customer_scope() -> None:
    result = _invoke_tool("hana.iyer@verdantfoods.com", None)

    assert result["status"] == "error"
    assert result["code"] == "unauthorized"


def test_denies_cross_customer_diagnostics(telemetry_dir: Path) -> None:
    (telemetry_dir / "hana.iyer@verdantfoods.com.json").write_text(
        json.dumps(_telemetry_payload(customer_id="ACC-1006")), encoding="utf-8"
    )

    result = _invoke_tool("hana.iyer@verdantfoods.com", "ACC-1007")

    assert result["status"] == "error"
    assert result["code"] == "unauthorized"
