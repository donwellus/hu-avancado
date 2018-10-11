import pytest
from app_factory import create_app


@pytest.fixture(scope='session')
def app():
    a = create_app()
    a.testing = True
    return a


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def resp(client):
    return client.get('/')


def test_status_code(resp):
    assert resp.status_code == 200


def test_content(resp):
    assert 'Hello World' in resp.get_data(as_text=True)
