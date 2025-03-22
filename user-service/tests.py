from fastapi.testclient import TestClient
from app.main import app
from app.database import SessionLocal
from app.models import User

client = TestClient(app)

def get_token():
    response = client.post("/users/login", data={
        "username": "testuser2",
        "password": "securepass"
    })
    assert response.status_code == 200
    return response.json()["access_token"]

def test_register_user():
    response = client.post("/users/register", json={
        "username": "testuser2",
        "email": "test2@mail.com",
        "password": "securepass"
    })
    assert response.status_code == 200
    assert response.json()["message"] == "User created"

def test_login_user():
    response = client.post("/users/login", data={
        "username": "testuser2",
        "password": "securepass"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_get_profile():
    token = get_token()
    response = client.get("/users/profile", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["username"] == "testuser2"

def test_delete_user():
    token = get_token()
    response = client.delete("/users/delete", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["message"] == "User deleted"

def test_database_user_creation():
    db = SessionLocal()
    user = User(username="dbuser", email="dbuser@test.com")
    user.set_password("password123")
    db.add(user)
    db.commit()
    fetched_user = db.query(User).filter_by(username="dbuser").first()
    assert fetched_user is not None
    assert fetched_user.username == "dbuser"
    db.delete(fetched_user)
    db.commit()
    db.close()
