"""Diagnostic tools that agents can use to obtain telemetry evidence."""

from datetime import datetime
from typing import Any, Literal

from langchain.tools import ToolRuntime, tool
from loguru import logger
from pydantic import BaseModel, EmailStr, Field, ValidationError

from app.config import get_settings


class Provisioning(BaseModel):
    scim_status: str
    last_scim_sync: datetime
    last_scim_result: str


class Network(BaseModel):
    ssid: str
    captive_portal_detected: bool
    udp_443_reachable: bool
    tcp_443_reachable: bool


class ClientDiagnostics(BaseModel):
    customer_id: str
    os: str
    client_version: str
    last_connect_attempt: datetime
    last_error: str
    provisioning: Provisioning
    network: Network
    user_email: EmailStr
    queried_at: datetime


class GetClientDiagnosticsInput(BaseModel):
    """The only argument the model is allowed to provide for this tool."""

    user_email: EmailStr = Field(
        description="Email address of the Cato Client user whose diagnostics are needed."
    )


class ToolEvidence(BaseModel):
    """A telemetry result that a later agent can cite."""

    status: Literal["ok"] = "ok"
    tool_name: Literal["get_client_diagnostics"] = "get_client_diagnostics"
    source: Literal["telemetry:client_diagnostics"] = "telemetry:client_diagnostics"
    observed_at: datetime
    query: dict[str, str]
    facts: dict[str, Any]
    result: ClientDiagnostics


class ToolError(BaseModel):
    """A safe, structured failure that the agent can handle without guessing."""

    status: Literal["error"] = "error"
    tool_name: Literal["get_client_diagnostics"] = "get_client_diagnostics"
    code: Literal["not_found", "invalid_telemetry", "unauthorized"]
    message: str


def _load_client_diagnostics(user_email: EmailStr) -> ClientDiagnostics | ToolError:
    """Temporary file-backed adapter; Phase 2 will replace it with a repository."""
    client_diag_path = (
        get_settings().data_path / "telemetry" / "clients" / f"{user_email}.json"
    )
    try:
        return ClientDiagnostics.model_validate_json(
            client_diag_path.read_text(encoding="utf-8")
        )
    except FileNotFoundError:
        return ToolError(
            code="not_found",
            message="No Cato Client diagnostics are available for that user.",
        )
    except ValidationError:
        logger.warning("Client diagnostics telemetry failed schema validation")
        return ToolError(
            code="invalid_telemetry",
            message="Client diagnostics are temporarily unavailable due to invalid telemetry.",
        )


def _trusted_customer_id(runtime: ToolRuntime) -> str | None:
    """Read graph-injected customer scope, never an LLM tool argument."""
    context = runtime.context
    if isinstance(context, dict):
        return context.get("customer_id")
    return getattr(context, "customer_id", None)


@tool(args_schema=GetClientDiagnosticsInput)
def get_client_diagnostics(user_email: EmailStr, runtime: ToolRuntime) -> dict[str, Any]:
    """Get Cato Client evidence for the verified customer only.

    Use for Cato Client connection, authentication, SCIM, captive-portal, or
    UDP/TCP 443 reachability issues. Do not use it outside the active customer.
    """
    authorized_customer_id = _trusted_customer_id(runtime)
    if not authorized_customer_id:
        logger.error("Diagnostics tool called without trusted customer scope")
        return ToolError(
            code="unauthorized",
            message="Client diagnostics require an identified customer.",
        ).model_dump(mode="json")

    diagnostics = _load_client_diagnostics(user_email)
    if isinstance(diagnostics, ToolError):
        return diagnostics.model_dump(mode="json")

    if diagnostics.customer_id != authorized_customer_id:
        logger.warning("Diagnostics tool denied a cross-customer request")
        return ToolError(
            code="unauthorized",
            message="Client diagnostics are not available for the active customer.",
        ).model_dump(mode="json")

    evidence = ToolEvidence(
        observed_at=diagnostics.queried_at,
        query={"user_email": str(user_email)},
        facts={
            "last_error": diagnostics.last_error,
            "captive_portal_detected": diagnostics.network.captive_portal_detected,
            "udp_443_reachable": diagnostics.network.udp_443_reachable,
            "tcp_443_reachable": diagnostics.network.tcp_443_reachable,
            "scim_status": diagnostics.provisioning.scim_status,
        },
        result=diagnostics,
    )
    return evidence.model_dump(mode="json")


if __name__ == "__main__":
    # Manual adapter check. LangGraph calls the decorated tool with context.
    print(_load_client_diagnostics("hana.iyer@verdantfoods.com"))
