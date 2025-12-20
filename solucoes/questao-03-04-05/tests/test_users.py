def test_create_user_without_password(client):
    payload = {
        "name": "Usuario Teste",
        "email": "teste_api@example.com",
        "role_id": 1
    }

    response = client.post("/users", json=payload)

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["name"] == payload["name"]
    assert data["email"] == payload["email"]
    assert data["role_id"] == payload["role_id"]
    assert "created_at" in data


def test_create_user_missing_required_field(client):
    payload = {
        "email": "sem_nome@example.com",
        "role_id": 1
    }

    response = client.post("/users", json=payload)

    assert response.status_code in (400, 422)
