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

def test_create_user():
    data = {
        "fname": "John",
        "lname": "Doe",
        "email": "john.doe@example.com",
        "password": "securepassword"
    }
    response = client.post("/users/", json=data, headers={"Content-Type": "application/json"})
    print(response.json())
    assert response.status_code == 201
    assert response.json()["user"]["email"] == "john.doe@example.com"

def test_get_all_users():
    response = client.get("/users/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert len(response.json()["users"]) > 0

def test_get_user_by_id():
    user_id = 1
    response = client.get(f"/users/{user_id}/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["user"]["id"] == user_id

def test_update_user():
    user_id = 1
    update_data = {"fname": "UpdatedName"}
    response = client.patch(f"/users/{user_id}/", json=update_data, headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["user"]["fname"] == "UpdatedName"

def test_delete_user():
    user_id = 1
    response = client.delete(f"/users/{user_id}/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json()["user"]["id"] == user_id
