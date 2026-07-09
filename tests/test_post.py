"""
Tests for Posts API
"""
import pytest
from utils.assertions import (
    verify_status_code, 
    verify_response_key_exists,
    verify_response_type,
    verify_array_not_empty,
    verify_response_contains
)


@pytest.mark.smoke
def test_get_all_posts(post_api):
    """Test retrieving all posts"""
    response = post_api.get_posts()
    verify_status_code(response, 200)
    verify_response_type(response, list)
    verify_array_not_empty(response)


@pytest.mark.smoke
def test_get_posts_contain_required_fields(post_api):
    """Test that posts contain required fields"""
    response = post_api.get_posts()
    verify_status_code(response, 200)
    verify_array_not_empty(response)
    # Verify first post has required fields
    posts = response.json()
    first_post = posts[0]
    for key in ["id", "userId", "title", "body"]:
        assert key in first_post, f"Missing required field: {key}"


@pytest.mark.sanity
def test_create_post(post_api, post_payload):
    """Test creating a new post"""
    response = post_api.create_post(post_payload)
    verify_status_code(response, 201)
    verify_response_key_exists(response, "id")
    data = response.json()
    verify_response_contains(response, {
        "title": post_payload["title"],
        "body": post_payload["body"],
        "userId": post_payload["userId"]
    })


@pytest.mark.sanity
def test_update_post(post_api, post_id, post_payload):
    """Test updating a post"""
    updated_payload = {**post_payload, "title": "Updated Title"}
    response = post_api.update_post(post_id, updated_payload)
    verify_status_code(response, 200)
    verify_response_contains(response, {"title": "Updated Title"})


@pytest.mark.sanity
def test_delete_post(post_api, post_id):
    """Test deleting a post"""
    response = post_api.delete_post(post_id)
    verify_status_code(response, 200)


@pytest.mark.regression
def test_get_post_by_id(post_api, post_id):
    """Test retrieving a specific post by ID"""
    response = post_api.get_posts()
    assert response.status_code == 200
    posts = response.json()
    post = next((p for p in posts if p["id"] == post_id), None)
    assert post is not None, f"Post with ID {post_id} not found"