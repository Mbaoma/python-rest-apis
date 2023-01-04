import pytest
from app import app as test_app

@pytest.fixture()
def app():
        yield test_app

@pytest.fixture()
def client(app):
    return app.test_client()