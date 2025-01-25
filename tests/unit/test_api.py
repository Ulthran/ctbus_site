import pytest
from app.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200


def test_favicon(client):
    response = client.get("/favicon.ico")
    assert response.status_code == 200


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_past_work(client):
    response = client.get("/past_work")
    assert response.status_code == 200


def test_pcmp(client):
    response = client.get("/pcmp")
    assert response.status_code == 200


def test_music(client):
    response = client.get("/music")
    assert response.status_code == 200


def test_blog(client):
    response = client.get("/blog")
    assert response.status_code == 200


def test_projects(client):
    response = client.get("/projects")
    assert response.status_code == 200


def test_sports(client):
    response = client.get("/sports")
    assert response.status_code == 200


def test_education(client):
    response = client.get("/education")
    assert response.status_code == 200


def test_certifications(client):
    response = client.get("/certifications")
    assert response.status_code == 200


def test_favorite_number(client):
    response = client.get("/favorite-number")
    assert response.status_code == 200


def test_session(client):
    response = client.get("/session")
    assert response.status_code == 200


def test_sitemap(client):
    response = client.get("/sitemap.xml")
    assert response.status_code == 200


def test_404(client):
    response = client.get("/this-is-not-a-real-page")
    assert response.status_code == 404
