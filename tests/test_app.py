import pytest
import app as app_module


@pytest.fixture
def client():
    app_module.app.config["TESTING"] = True
    app_module.app.config["DATABASE"] = ":memory:"
    with app_module.app.app_context():
        app_module.init_db()
    yield app_module.app.test_client()
