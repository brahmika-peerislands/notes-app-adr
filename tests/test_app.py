import pytest
import app as app_module


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    app_module.app.config["DATABASE"] = ":memory:"
    with app_module.app.app_context():
        app_module.init_db()
    yield app_module.app.test_client()


def test_db_tables_created(client):
    with app_module.app.app_context():
        db = app_module.get_db()
        cursor = db.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='notes'"
        )
        table = cursor.fetchone()
        assert table is not None, "notes table should exist after init_db()"
        cursor = db.execute("PRAGMA table_info(notes)")
        columns = {row[1] for row in cursor.fetchall()}
        assert "id" in columns
        assert "title" in columns
        assert "body" in columns


def test_create_note_returns_201(client):
    response = client.post(
        "/notes",
        json={"title": "Meeting notes", "body": "Discuss Q3 roadmap"},
    )
    assert response.status_code == 201
    assert "application/json" in response.content_type
    data = response.get_json()
    assert isinstance(data["id"], int)
    assert data["title"] == "Meeting notes"
    assert data["body"] == "Discuss Q3 roadmap"


def test_create_note_empty_title_returns_400(client):
    response = client.post("/notes", json={"body": "No title here"})
    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data


def test_list_notes_empty(client):
    response = client.get("/notes")
    assert response.status_code == 200
    assert "application/json" in response.content_type
    assert response.get_json() == []


def test_list_notes_returns_all(client):
    client.post("/notes", json={"title": "Note 1", "body": "Body 1"})
    client.post("/notes", json={"title": "Note 2", "body": "Body 2"})
    response = client.get("/notes")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]["title"] == "Note 1"
    assert data[1]["title"] == "Note 2"


def test_get_note_by_id_found(client):
    create_response = client.post(
        "/notes", json={"title": "Test note", "body": "Test body"}
    )
    note_id = create_response.get_json()["id"]
    response = client.get(f"/notes/{note_id}")
    assert response.status_code == 200
    assert "application/json" in response.content_type
    data = response.get_json()
    assert data["id"] == note_id
    assert data["title"] == "Test note"
    assert data["body"] == "Test body"


def test_get_note_by_id_not_found(client):
    response = client.get("/notes/9999")
    assert response.status_code == 404
    assert "application/json" in response.content_type
    data = response.get_json()
    assert data == {"error": "Note not found"}
