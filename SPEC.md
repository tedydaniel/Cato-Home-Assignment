# Cato AI Support Engineer — Technical Specification

## 1. Purpose and scope

Build a locally runnable, demo-ready, conversational support engineer for Cato
Networks. It will identify a customer from trusted account data, retrieve and
cite a pinned Cato Knowledge Base (KB) snapshot, inspect synthetic telemetry,
diagnose problems across multiple turns, perform simulated support actions, and
pause for human review of high-impact actions.

The system is intentionally a **decision-support and support-automation demo**.
It must never treat claims in chat as trusted identity, entitlement, authority,
or technical evidence.

## 2. Architecture decisions

| Area | Decision |
| --- | --- |
| Frontend | Next.js + TypeScript + Tailwind CSS + shadcn/ui |
| Backend | Python 3.12, FastAPI, Pydantic v2, SQLAlchemy + Alembic |
| Workflow runtime | LangGraph (Python), with a PostgreSQL checkpointer |
| LLM integration | Provider adapter; initial implementation uses OpenAI through LangChain. Models are environment-configured. |
| Tracing | LangSmith for graph/model/tool traces, plus a first-party immutable database audit trail for the reviewer UI and replay. |
| Primary database | PostgreSQL 16 with `pgvector` and built-in full-text search |
| Background work | Explicit CLI commands for KB ingestion and evals; no queue in the demo stack |
| Retrieval | Hybrid lexical + vector search, reciprocal-rank fusion (RRF), metadata filtering, optional reranking |
| API streaming | Server-Sent Events (SSE) from backend to frontend |
| Packaging | Docker Compose, one container for each service described below |
| Testing | pytest, httpx, Playwright, deterministic policy tests, CLI eval runner |

Python is selected for the backend because LangGraph and PostgreSQL persistence
are first-class, well-supported Python workflows. The frontend remains
independently deployable TypeScript.

LangGraph checkpoints are durable workflow state, not the only application
record. PostgreSQL business tables remain authoritative for conversations,
messages, approvals, tickets, and reviewer-facing audit data.

## 3. Docker Compose services

| Service | Responsibilities | Persistent data |
| --- | --- | --- |
| `frontend` | Next.js customer chat, reviewer console, trace and approval views | none |
| `backend` | FastAPI REST/SSE API, LangGraph execution, typed tools, retrieval, policy enforcement | none; writes PostgreSQL |
| `postgres` | Application state, LangGraph checkpoints, KB corpus/indexes, audit trail | named volume `postgres_data` |

All secrets are supplied through `.env` (never committed). A `docker compose up
--build` path must run the UI without requiring a fresh KB crawl; the committed
KB snapshot is loaded by a seed/import job. KB refreshes and eval runs are
explicit CLI commands in this demo, rather than queued background jobs.

## 4. Agent graph

The graph uses a stable `thread_id = conversation_id` and PostgreSQL-backed
checkpoints. Each node has Pydantic-defined input/output state and logs an audit
event. Graph state includes only redacted customer content.

```text
input
  -> sanitize_and_identify
  -> triage
  -> evidence_fanout (knowledge + diagnostics)
  -> resolve
  -> validate_response
  -> [approval_wait | persist_and_reply]
```

### Nodes / specialised agents

1. **Sanitize & Identity (deterministic service)** — redact credentials before
   persistence/tracing; resolve account by trusted account ID or verified email;
   ignore asserted tier/authority; detect injection indicators.
2. **Triage agent** — determine intent, urgency, site/scope gaps, and the next
   diagnostic/retrieval plan. It can ask a narrow scoping question.
3. **Knowledge agent** — retrieves KB and internal-policy evidence. It returns
   structured claims and citations only; it does not draft customer advice.
4. **Diagnostics agent** — invokes allowlisted, Pydantic-validated telemetry,
   ticket, and account tools with timeouts. Every fact it returns names the
   source tool and result identifier.
5. **Resolution agent** — synthesizes the user-facing answer from validated
   evidence and proposes a typed action when appropriate.
6. **Guardrail/QA node** — validates redaction, citation coverage, evidence
   attribution, policy constraints, and action authorization before output.

The knowledge and diagnostics agents run in parallel where both are required.
If retrieval fails or falls below its confidence threshold, the agent says it
cannot verify the technical claim and routes to a human/ticket rather than
inventing an answer. If telemetry fails, it reports the unavailable evidence and
continues with safe scoping and KB-grounded guidance.

### Human approval interrupt

Credits/refunds, MFA resets, and security-verdict overrides create an
`approval_request` row and call LangGraph's interrupt mechanism. The graph
stops; it does not poll in memory. The reviewer may approve, edit, or reject
through the UI. The backend resumes the exact `conversation_id` after persisting
that decision. The customer can continue receiving non-action answers while an
approval is pending.

## 5. Trust, guardrails, and trace handling

These rules are deterministic code, not instructions the LLM is trusted to
follow:

- Redact secrets before database writes, LangGraph checkpoints, LangSmith, logs,
  or chat echoing.
- Check identity, registered-admin status, tier, and SLA only against account
  data. Ticket body and chat text are untrusted.
- Validate every tool input/output with Pydantic, enforce allowlists/timeouts,
  and record a tool evidence identifier.
- Never commit a credit/refund without an approved request.
- Never reset MFA without the policy-defined identity verification.
- Never perform a malware/C2 verdict override; route it according to policy.
- Block technical replies lacking KB citations, except clearly labelled
  telemetry evidence or a clear no-coverage escalation.

LangSmith is configured with redacted inputs/outputs only and tagged with the
conversation ID, scenario/eval ID when applicable, agent node, and git revision.
The database `trace_events` audit log is retained as the source used by the UI
and transcript replay; LangSmith complements it rather than replacing it.

## 6. Retrieval and knowledge ingestion

The KB ingestion CLI provides an idempotent pipeline:

1. Crawl only English Cato KB pages, respecting `robots.txt`, a declared user
   agent, and rate limits.
2. Parse article title, canonical URL/slug, headings, body, last-updated value,
   and content hash.
3. Chunk by heading while preserving article/section metadata and overlap.
4. Generate embeddings; add PostgreSQL full-text indexes and vector indexes.
5. At query time, retrieve lexical and semantic candidates, fuse with RRF,
   filter on source/type/language, then rerank the fused shortlist.
6. Return citations as article URL/slug, section, chunk ID, snapshot date, and
   retrieval score.

The repository includes a pinned KB manifest: crawl date, crawler version,
canonical URL, metadata, and per-article hash. The running app imports this
snapshot, so crawling is not a startup requirement.

## 7. Core persisted entities

- `accounts`, `tickets`, `ticket_events`
- `conversations`, `messages`, `conversation_participants`
- `approvals`, `proposed_actions`, `simulated_action_events`
- `tool_calls`, `tool_evidence`, `trace_events`
- `kb_snapshots`, `kb_articles`, `kb_chunks`, `retrieval_runs`
- LangGraph checkpoint tables managed by its PostgreSQL checkpointer
- `eval_runs`, `eval_case_results`, `daily_reports`

Every event stores UTC timestamps. Demo telemetry's frozen timestamp
`2026-08-28T17:00:00Z` is presented as the support system's operational “now”.

## 8. API and UI surface

Backend endpoints, initially:

- `POST /api/conversations` — create a customer conversation.
- `POST /api/conversations/{id}/messages` — submit a customer message.
- `GET /api/conversations/{id}/events` — SSE stream of agent status and reply
  events.
- `GET /api/conversations/{id}` — state, messages, cited evidence, and context.
- `GET /api/conversations/{id}/trace` — redacted durable trace.
- `GET /api/approvals` — reviewer queue.
- `POST /api/approvals/{id}/decision` — approve, edit, or reject then resume.
- `POST /api/evals/run` and `GET /api/evals/{id}` — local eval execution/results.
- `GET /api/reports/daily` — generated daily operations report.

The frontend has two routes:

- `/chat` — customer chat with streaming status, citations, and transparent
  “waiting for review” states.
- `/reviewer` — trusted account context, tool evidence, cited sources, graph/audit
  trace, approval queue, and daily operations dashboard.

## 9. Evaluation and acceptance criteria

The CI-runnable evaluation suite must include:

- retrieval Recall@k and MRR across `data/eval/questions.jsonl`;
- same-code-path generation of `answers.md` with citations, top chunks/scores,
  latency, token cost, and snapshot date;
- scripted replay of all 12 scenarios without passing expected behaviour into the
  inference context;
- groundedness, citation, action, tool-use, and guardrail scoring;
- deterministic tests for secret redaction, injection detection, identity/tier
  checks, tool schemas/timeouts, and approval enforcement;
- persistence tests proving an approval can be resumed after a backend restart.

## 10. Initial environment variables

```dotenv
POSTGRES_URL=postgresql+psycopg://...
OPENAI_API_KEY=
OPENAI_MODEL=
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=cato-support-engineer
LANGSMITH_ENDPOINT=
KB_SNAPSHOT_DATE=
```

## 11. Implementation sequence

1. Scaffold Compose, FastAPI, Next.js, and PostgreSQL migrations.
2. Import supplied account/ticket/policy/telemetry data and implement typed tools.
3. Implement the crawler and pinned KB ingestion/retrieval pipeline.
4. Build the LangGraph graph, checkpointer, durable audit traces, and guardrails.
5. Build chat and reviewer UI, including approval interrupts/resume.
6. Add eval harness, reports, recorded demos, documentation, and CI.
