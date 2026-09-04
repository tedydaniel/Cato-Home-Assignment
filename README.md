# Cato AI Support Engineer

Phase 1 provides a five-service local foundation: Next.js frontend, FastAPI backend, PostgreSQL 16 with pgvector, Redis, and a Celery worker. The full design is in [SPEC.md](SPEC.md).

## Run

1. Copy `.env.example` to `.env` and replace the password in both `POSTGRES_PASSWORD` and `POSTGRES_URL`.
2. Run `docker compose up --build`.
3. Visit <http://localhost:3000>; API docs are at <http://localhost:8000/docs>.

`data/` is mounted read-only in the backend and worker. Phase 2 will import account/ticket/policy data and expose telemetry exclusively through typed tools.
