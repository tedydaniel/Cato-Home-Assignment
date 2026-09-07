# Operational runbook

1. Copy `.env.example` to `.env` and set `POSTGRES_PASSWORD` and `OPENAI_API_KEY`.
2. Run `docker compose up --build`.
3. Run `docker compose --profile tools run --rm ingest` to hash-verify and index the committed KB snapshot. To deliberately refresh from Cato's public KB, run `docker compose --profile tools run --rm ingest python -m scripts.ingest_kb --refresh-snapshot`.
4. Open `http://localhost:3000`; API health is `http://localhost:8000/health/ready`.
5. For retrieval metrics run `uv run --directory backend python -m scripts.evaluate_retrieval` after ingestion.
6. For evaluator transcripts run `uv run --directory backend python -m scripts.generate_answers`.
7. For the two-channel daily report run `uv run --directory backend python -m scripts.daily_operations_report`; it writes `reports/daily_operations.md` and `reports/daily_operations.csv`.

If the knowledge index is unavailable, the response agent refuses technical guidance. If telemetry is unavailable, it states that limitation rather than inferring values. Pending protected actions and LangGraph checkpoints remain in PostgreSQL. Approving or rejecting a request in Tasks & alerts resumes the exact interrupted conversation and records a simulated outcome; editing keeps the request pending for a later final decision.
