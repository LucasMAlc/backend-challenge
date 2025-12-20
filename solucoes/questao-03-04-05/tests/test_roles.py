def test_get_role_by_id_success(client):
    response = client.get("/roles/1")

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert "description" in data
    assert data["id"] == 1


def test_get_role_by_id_not_found(client):
    response = client.get("/roles/9999")

    assert response.status_code == 404
