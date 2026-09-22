# Review Checklist — Notes API

Use this checklist when reviewing changes to the Notes API.

## FR-1: POST /notes (Create Note)

- [ ] POST /notes with valid `{title, body}` returns HTTP **201**
- [ ] Response body contains `id` (integer), `title`, and `body` fields
- [ ] Response `Content-Type` is `application/json`
- [ ] POST /notes with missing or empty `title` returns HTTP **400**
- [ ] 400 response body contains an `error` field
- [ ] No string interpolation in SQL (parameterised query used)

## FR-2: GET /notes (List Notes)

- [ ] GET /notes returns HTTP **200** in all non-error cases
- [ ] Response is a JSON array
- [ ] Empty store returns `[]` (not `null`, not omitted)
- [ ] Response `Content-Type` is `application/json`
- [ ] Each note object contains `id`, `title`, `body` fields

## FR-3: GET /notes/<id> (Get Note by ID)

- [ ] GET /notes/<id> for an existing note returns HTTP **200**
- [ ] Response body contains `id`, `title`, `body` with correct values
- [ ] GET /notes/<id> for a non-existent id returns HTTP **404**
- [ ] 404 response body is exactly `{"error": "Note not found"}`
- [ ] Response `Content-Type` is `application/json` for all outcomes

## FR-4: SQLite Persistence

- [ ] `notes` table schema: `id INTEGER PRIMARY KEY AUTOINCREMENT`, `title TEXT NOT NULL`, `body TEXT NOT NULL`
- [ ] `init_db()` is idempotent (`CREATE TABLE IF NOT EXISTS`)
- [ ] `get_db()` uses `app.config.get('DATABASE', DATABASE)` so tests can inject `:memory:`
- [ ] `notes.db` is in `.gitignore`

## FR-5: ADR-0001 before persistence code

- [ ] `docs/adr/ADR-0001-local-persistence.md` exists
- [ ] ADR contains `Status: Accepted`
- [ ] ADR contains the exact string `Use SQLite for note persistence in v1` in the Decision section

## FR-6: Decoy ADR

- [ ] `scratch/random/ADR-0099-use-postgres.md` exists
- [ ] File contains `Postgres` or `PostgreSQL`
- [ ] File is NOT cited as the authoritative persistence decision

## FR-7: README references ADR-0001

- [ ] `README.md` exists at repo root
- [ ] README contains `ADR-0001` in a context linking it to the persistence approach
- [ ] README links to `docs/adr/ADR-0001-local-persistence.md`

## FR-8: Test coverage

- [ ] `tests/test_app.py` has a `client` fixture with `TESTING=True` and `DATABASE=':memory:'`
- [ ] Happy-path test: create a note, retrieve it by id, verify title and body match
- [ ] `pytest --cov=app --cov-fail-under=80` passes (>=80% diff coverage)
