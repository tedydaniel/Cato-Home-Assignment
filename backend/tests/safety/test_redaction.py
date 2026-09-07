from app.safety.redaction import redact_secrets


def test_redaction_removes_supported_secret_values() -> None:
    result = redact_secrets("PSK: hunter2 and API key=sk-secret password: no-echo")

    assert "hunter2" not in result
    assert "sk-secret" not in result
    assert "no-echo" not in result
    assert result.count("[REDACTED]") == 3
