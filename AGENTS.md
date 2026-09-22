# Local Notes HTTP API — Project Context for AI Agents

## Overview

This is a minimal REST API for managing personal notes. Built with Python 3.12, Flask, and SQLite (via the stdlib `sqlite3` module). Single-module layout: all application code lives in `app.py`.

## Tech stack

- **Python 3.12** — pinned in `.python-version`
- **Flask** — HTTP framework and test client
- **sqlite3** (stdlib) — persistence; no ORM
- **pytest + pytest-cov** — test runner with coverage gate
- **ruff** — formatting (`ruff format`) and linting (`ruff check`)
- **mypy** — static type checking
- **pip-audit** — dependency vulnerability scanning
- **pre-commit** — local commit hooks (arm with `pre-commit install`)

## Key files

| File | Purpose |
|------|---------|
| `app.py` | Flask app, route handlers, persistence helpers |
| `tests/test_app.py` | pytest integration tests |
| `requirements.txt` | Pinned dependencies |
| `.python-version` | pyenv Python version pin (3.12) |
| `docs/adr/ADR-0001-local-persistence.md` | Persistence architecture decision record (Status: Accepted) |
| `scratch/random/ADR-0099-use-postgres.md` | Rejected alternative (decoy for brownfield evaluation) |

## Quality gate commands

Run all gates locally in this order:

```bash
ruff format --check .
ruff check .
mypy app.py --ignore-missing-imports
pytest --cov=app --cov-fail-under=80
pip-audit --requirement requirements.txt
```

## Test fixture setup

Tests use an in-memory SQLite database. The `client` fixture in `tests/test_app.py`:
- Sets `TESTING=True` on the Flask app
- Overrides `DATABASE` to `':memory:'` for test isolation
- Calls `init_db()` inside an app context to create the schema
- Yields a fresh `app.test_client()` per test

Each test gets an isolated, empty database.

## See also

- `.claude/skills/run-gates.md` — run all quality gates
- `.claude/skills/add-endpoint.md` — add a new REST endpoint
- `.claude/skills/review-checklist.md` — review checklist from spec DoDs
