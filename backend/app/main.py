from fastapi import FastAPI, HTTPException
from app.db import database_is_ready

app = FastAPI(title="Cato AI Support Engineer API", version="0.1.0")

@app.get("/health/live", tags=["health"])
def liveness() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/health/ready", tags=["health"])
def readiness() -> dict[str, str]:
    if not database_is_ready():
        raise HTTPException(status_code=503, detail="database unavailable")
    return {"status": "ready"}

@app.get("/api")
def api_root() -> dict[str, str]:
    return {"service": "cato-support-engineer-api", "phase": "foundation"}
