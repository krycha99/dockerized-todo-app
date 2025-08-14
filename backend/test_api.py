import os
import pytest
from pymongo import MongoClient
from app import app

@pytest.fixture
def client(monkeypatch):
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017/testdb")
    
    test_client = app.test_client()
    test_db = MongoClient(mongo_uri)["testdb"]
    
    test_db["tasks"].delete_many({})
    
    monkeypatch.setattr("app.tasks_collection", test_db["tasks"])

    return test_client


def test_home(client):
    rv = client.get("/")
    assert rv.status_code == 200


def test_add_task(client):
    rv = client.post("/tasks", json={"title": "Test Task"})
    assert rv.status_code == 201

    from app import tasks_collection
    task = tasks_collection.find_one({"title": "Test Task"})
    assert task is not None


def test_add_task_without_title(client):
    rv = client.post("/tasks", json={})
    assert rv.status_code == 400


def test_get_tasks(client):
    from app import tasks_collection
    tasks_collection.insert_one({"title": "Sample", "done": False})

    rv = client.get("/tasks")
    assert rv.status_code == 200
    data = rv.get_json()
    assert any(task["title"] == "Sample" for task in data)


def test_delete_task(client):
    from app import tasks_collection
    tasks_collection.insert_one({"title": "ToDelete", "done": False})

    rv = client.delete("/tasks/ToDelete")
    assert rv.status_code == 200
    assert tasks_collection.find_one({"title": "ToDelete"}) is None


def test_delete_nonexistent_task(client):
    rv = client.delete("/tasks/NoTaskHere")
    assert rv.status_code == 404