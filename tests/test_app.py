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
