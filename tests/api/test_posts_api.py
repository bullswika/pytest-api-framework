# Jiacheng
# @Time: 2025/12/12
# @Email: bullswika@outlook.com
# @File: test_posts_api.py

import pytest

@pytest.mark.smoke
def test_get_single_post(api_client):
    resp = api_client.get("/posts/1")
    assert resp.status_code == 200

    data = resp.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data

@pytest.mark.regression
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_parametrized(api_client, post_id):
    resp = api_client.get(f"/posts/{post_id}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == post_id

@pytest.mark.smoke
def test_create_post(api_client):
    payload = {
        "title": "jc test title",
        "body": "pytest + requests demo",
        "user_id": 1
    }
    resp = api_client.post("/posts", json=payload)
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["user_id"] == payload["user_id"]