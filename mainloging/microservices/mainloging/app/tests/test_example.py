from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_mainloging():
    response = client.post("/mainloging/", json={"name": "Test Mainloging", "description": "A mainloging for testing"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Mainloging"

def test_read_mainloging():
    response = client.post("/mainloging/", json={"name": "Test Mainloging", "description": "A mainloging for testing"})
    item_id = response.json()["id"]
    response = client.get(f"/mainloging/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Mainloging"

def test_update_mainloging():
    response = client.post("/mainloging/", json={"name": "Test Mainloging", "description": "A mainloging for testing"})
    item_id = response.json()["id"]
    response = client.put(f"/mainloging/{item_id}", json={"name": "Updated Mainloging", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Mainloging"

def test_delete_mainloging():
    response = client.post("/mainloging/", json={"name": "Test Mainloging", "description": "A mainloging for testing"})
    item_id = response.json()["id"]
    response = client.delete(f"/mainloging/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Mainloging"
