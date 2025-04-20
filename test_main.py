import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@pytest.fixture(scope="module")
def test_client():
    yield client


def test_create_contact(test_client):
    response = test_client.post("/contacts/", json={"full_name": "John Doe", "phone_number": "1234567890"})
    assert response.status_code == 200
    assert response.json()["full_name"] == "John Doe"


def test_search_contact(test_client):
    response = test_client.get("/contacts/search/?query=John")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_read_contacts(test_client):
    response = test_client.get("/contacts/")
    assert response.status_code == 200
