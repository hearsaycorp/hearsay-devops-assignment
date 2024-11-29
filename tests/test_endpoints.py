import pytest
from flask_api.app import app as api


@pytest.fixture()
def app():
    app = api
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_request_root(client):
    response = client.get("/")
    assert "Hello from Flask!" in str(response.data)
    assert 200 == response.status_code


def test_request_coffee(client):
    response = client.get("/coffee")
    assert "Let's make some tea!" in str(response.data)
    assert 418 == response.status_code
