import pytest
from app import create_app
from app.config.settings import settings
from fastapi.testclient import TestClient

@pytest.fixture
def app():
    return create_app()

@pytest.fixture
def client(app):
    return TestClient(app)