"""
Tests for Comments API
"""
import pytest
from utils.assertions import (
    verify_status_code,
    verify_response_key_exists,
    verify_response_type,
    verify_array_not_empty,
    verify_array_contains_key
)


@pytest.mark.smoke
def test_get_all_comments(comments_api):
    """Test retrieving all comments"""
    response = comments_api.get_comments()
    verify_status_code(response, 200)
    verify_response_type(response, list)
    verify_array_not_empty(response)


@pytest.mark.smoke
def test_get_all_comments_have_required_fields(comments_api):
    """Test that all comments have required fields"""
    response = comments_api.get_comments()
    verify_status_code(response, 200)
    for field in ["id", "postId", "name", "email", "body"]:
        verify_array_contains_key(response, field)


@pytest.mark.sanity
def test_get_single_comment(comments_api, comment_id):
    """Test retrieving a single comment"""
    response = comments_api.get_comment(comment_id)
    verify_status_code(response, 200)
    verify_response_key_exists(response, "id")
    data = response.json()
    assert data["id"] == comment_id


@pytest.mark.sanity
def test_get_comments_by_post(comments_api):
    """Test retrieving comments for a specific post"""
    response = comments_api.get_post_comments(post_id=1)
    verify_status_code(response, 200)
    verify_response_type(response, list)
    # Check that all returned comments are for the specified post
    comments = response.json()
    for comment in comments:
        assert comment["postId"] == 1, f"Comment has wrong postId: {comment['postId']}"


@pytest.mark.regression
def test_create_comment(comments_api, comment_payload):
    """Test creating a new comment"""
    response = comments_api.create_comment(comment_payload)
    verify_status_code(response, 201)
    verify_response_key_exists(response, "id")


@pytest.mark.regression
def test_update_comment(comments_api, comment_id, comment_payload):
    """Test updating a comment"""
    updated_payload = {**comment_payload, "name": "Updated Comment"}
    response = comments_api.update_comment(comment_id, updated_payload)
    verify_status_code(response, 200)


@pytest.mark.regression
def test_delete_comment(comments_api, comment_id):
    """Test deleting a comment"""
    response = comments_api.delete_comment(comment_id)
    verify_status_code(response, 200)
