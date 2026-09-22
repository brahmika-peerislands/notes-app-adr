# Local Notes HTTP API

A minimal REST API for managing personal notes, built with Python 3.12, Flask, and SQLite.

## Quick start

```bash
pip install -r requirements.txt
python app.py
```

The server starts on http://localhost:5000.

## API endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | /notes | Create a note |
| GET | /notes | List all notes |
| GET | /notes/\<id\> | Get a note by ID |

## Architecture decision

Persistence follows [ADR-0001: Local Persistence for Notes](docs/adr/ADR-0001-local-persistence.md).

The decision to use SQLite (via Python's `sqlite3` standard library) was made before any persistence code was written, as required by the project's architecture governance process.

## Running the tests

```bash
pytest --cov=app --cov-fail-under=80
```
