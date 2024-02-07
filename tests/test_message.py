from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from main import app, get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

async def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_message():
    data = {
        "text": "My Message",
        "room_id": 1,
        "created_by": 1,
    }
    response = client.post("/messages/", json=data, headers={"Content-Type": "application/json"})
    print(response.json())
    assert response.status_code == 201
    assert response.json()["message"]["text"] == "My Message"

def test_get_all_messages():
    response = client.get("/messages/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert len(response.json()["messages"]) > 0

def test_get_message_by_id():
    message_id = 1
    response = client.get(f"/messages/{message_id}/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["message"]["id"] == message_id

def test_update_message():
    message_id = 1
    update_data = {"text": "Updated Text"}
    response = client.patch(f"/messages/{message_id}/", json=update_data, headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["message"]["text"] == "Updated Text"

def test_delete_message():
    message_id = 1
    response = client.delete(f"/messages/{message_id}/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["message"]["id"] == message_id
