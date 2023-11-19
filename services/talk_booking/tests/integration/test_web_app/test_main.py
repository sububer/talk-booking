import pytest
from starlette.testclient import TestClient

from web_app.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_health_check(client):
    """
    GIVEN a FastAPI application
    WHEN health check endpoint is called with GET
    THEN response with status 200 and status OK is returned
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
