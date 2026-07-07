import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def post_payload():

    return {
        "title": "foo",
        "userId": 1,
        "body": "bar"
    }

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    # assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_post(payload):
    response = requests.post(f"{BASE_URL}/posts", json=post_payload)
    assert response.status_code == 201