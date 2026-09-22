# Add a New Flask Endpoint

Use this skill when adding a new HTTP endpoint to the Notes API.

## Pattern (TDD: test first, then implement)

### 1. Write the test first (in tests/test_app.py)

Add a test function that uses the `client` fixture:

```python
def test_my_new_endpoint(client):
    response = client.METHOD("/path", json={...})
    assert response.status_code == EXPECTED_STATUS
    data = response.get_json()
    assert data["field"] == expected_value
```

Run `pytest -k test_my_new_endpoint` — it should **fail** (red phase).

### 2. Add the route to app.py

```python
@app.route("/path", methods=["METHOD"])
def my_handler():
    db = get_db()
    # Use parameterised SQL — never interpolate values into SQL strings
    row = db.execute("SELECT ... WHERE id = ?", (value,)).fetchone()
    if row is None:
        return jsonify({"error": "Not found"}), 404
    db.execute("INSERT INTO notes (...) VALUES (?)", (value,))
    db.commit()
    return jsonify({...}), 200
```

### 3. Run the test again — it should pass (green phase)

```bash
pytest -k test_my_new_endpoint
```

### 4. Run all gates to verify no regressions

```bash
ruff format --check .
ruff check .
mypy app.py --ignore-missing-imports
pytest --cov=app --cov-fail-under=80
```

## Notes

- Always use `get_db()` for the database connection — never open `sqlite3.connect(...)` directly in a handler.
- Always use parameterised SQL (`?` placeholders) — never interpolate user input into SQL strings.
- JSON responses must include `Content-Type: application/json` (Flask's `jsonify()` sets this automatically).
