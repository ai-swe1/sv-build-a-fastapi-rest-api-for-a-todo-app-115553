import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post(
        "/todos",
        json={"title": "Test Todo", "description": "This is a test todo item"}
    )
    assert response.status_code == 201

def test_get_all_todos():
    response = client.get(
        "/todos"
    )
    assert response.status_code == 200

def test_get_single_todo():
    response = client.get(
        "/todos/1"
    )
    assert response.status_code == 200

def test_update_todo():
    response = client.put(
        "/todos/1",
        json={"title": "Updated Test Todo", "description": "This is an updated test todo item"}
    )
    assert response.status_code == 200

def test_delete_todo():
    response = client.delete(
        "/todos/1"
    )
    assert response.status_code == 204