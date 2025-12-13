# Jiacheng
# @Time: 2025/12/12
# @Email: bullswika@outlook.com
# @File: test_user_api.py
import allure
import pytest

@allure.title("GET /users returns a non-empty list")
@allure.story("Users API - Smoke")
@pytest.mark.smoke
def test_get_users_smoke(api_client):
    resp = api_client.get('/users')
    assert resp.status_code == 200

    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0

    first = data[0]
    assert "id" in first
    assert "name" in first
    assert "email" in first

@pytest.mark.smoke
@pytest.mark.parametrize("user_id", [1,2,3])
def test_get_user_by_id_smoke(api_client,user_id):
    resp = api_client.get(f"/users/{user_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == user_id
    assert "name" in data
    assert "email" in data

@pytest.mark.regression
def test_get_user_not_found(api_client):
    invalid_user_id = 9999
    resp = api_client.get(f"/users/{invalid_user_id}")
    assert resp.status_code == 404


@allure.title("Create user successfully")
@allure.story("Users API - Core Flow")
@pytest.mark.regression
def test_create_user(api_client):
    payload ={
        "name":"john",
        "email":"john@hotmail.com"
    }
    resp = api_client.create_user(payload)
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert "id" in data
    assert data.get("name") == payload["name"]
    assert data.get("email") == payload["email"]


@allure.title("Create user with missing email should fail")
@allure.story("Users API - Negative")
@pytest.mark.regression
@pytest.mark.xfail(reason="Demo API accept invalid payload")
def test_create_user_missing_email(api_client):
    # Expected behavior: API should reject missing email
    payload = {
        "name":"Mart",
    }
    resp = api_client.create_user(payload)
    assert resp.status_code in (400,422)
    data = resp.json()
    assert "error" in data or "message" in data


@allure.title("Create user with invalid email should fail")
@allure.story("Users API - Negative")
@pytest.mark.regression
@pytest.mark.xfail(reason="Demo API accept invalid payload")
def test_create_user_invalid_emails_format(api_client):
    # Expected behavior: API should reject wrogn email format
    payload = {
        "name":"Mart",
        "email":"not-an-valid-email"
    }
    resp = api_client.create_user(payload)
    assert resp.status_code in (400,422)
    data = resp.json()
    assert "error" in data or "message" in data



@allure.title("Create user with empty name should be rejected")
@allure.story("Users API - Negative")
@pytest.mark.regression
@pytest.mark.xfail(reason="Demo API accept invalid payload")
def test_create_user_empty_name(api_client):
    # Expected behavior: API should reject empty string name
    payload = {
        "name":"",
        "email":"not-a-valid-email"
    }
    resp = api_client.create_user(payload)
    assert resp.status_code in (400,422)
    data = resp.json()
    assert "error" in data or "message" in data
