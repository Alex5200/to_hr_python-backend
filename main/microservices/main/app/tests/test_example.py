from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_main():
    response = client.post("/main/", json={"name": "Test Main", "description": "A main for testing"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Main"

def test_read_main():
    response = client.post("/main/", json={"name": "Test Main", "description": "A main for testing"})
    item_id = response.json()["id"]
    response = client.get(f"/main/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Main"

def test_update_main():
    response = client.post("/main/", json={"name": "Test Main", "description": "A main for testing"})
    item_id = response.json()["id"]
    response = client.put(f"/main/{item_id}", json={"name": "Updated Main", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Main"

def test_delete_main():
    response = client.post("/main/", json={"name": "Test Main", "description": "A main for testing"})
    item_id = response.json()["id"]
    response = client.delete(f"/main/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Main"
