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

def test_create_room():
    data = {
        "name": "Room 1",
        "created_by": 1,
    }
    response = client.post("/rooms/", json=data, headers={"Content-Type": "application/json"})
    print(response.json())
    assert response.status_code == 201
    assert response.json()["room"]["name"] == "Room 1"

def test_get_all_rooms():
    response = client.get("/rooms/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert len(response.json()["rooms"]) > 0

def test_get_room_by_id():
    room_id = 1
    response = client.get(f"/rooms/{room_id}/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["room"]["id"] == room_id

def test_update_room():
    room_id = 1
    update_data = {"name": "Room 2"}
    response = client.patch(f"/rooms/{room_id}/", json=update_data, headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["room"]["name"] == "Room 2"

def test_delete_room():
    room_id = 1
    response = client.delete(f"/rooms/{room_id}/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["room"]["id"] == room_id
