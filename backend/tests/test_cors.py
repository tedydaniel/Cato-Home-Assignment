from fastapi.testclient import TestClient

from app.main import app


def test_browser_origin_can_preflight_chat_requests() -> None:
    response = TestClient(app).options(
        "/api/conversations",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "POST",
        },
    )

    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"
