from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_admindata():
    response = client.post("/admindata/", json={"name": "Test Admindata", "description": "A admindata for testing"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Admindata"

def test_read_admindata():
    response = client.post("/admindata/", json={"name": "Test Admindata", "description": "A admindata for testing"})
    item_id = response.json()["id"]
    response = client.get(f"/admindata/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Admindata"

def test_update_admindata():
    response = client.post("/admindata/", json={"name": "Test Admindata", "description": "A admindata for testing"})
    item_id = response.json()["id"]
    response = client.put(f"/admindata/{item_id}", json={"name": "Updated Admindata", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Admindata"

def test_delete_admindata():
    response = client.post("/admindata/", json={"name": "Test Admindata", "description": "A admindata for testing"})
    item_id = response.json()["id"]
    response = client.delete(f"/admindata/{item_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Admindata"
