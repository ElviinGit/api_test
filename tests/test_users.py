"""
Tests for Users API
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
def test_get_all_users(users_api):
    """Test retrieving all users"""
    response = users_api.get_users()
    verify_status_code(response, 200)
    verify_response_type(response, list)
    verify_array_not_empty(response)


@pytest.mark.smoke
def test_get_all_users_have_id(users_api):
    """Test that all users have id field"""
    response = users_api.get_users()
    verify_status_code(response, 200)
    verify_array_contains_key(response, "id")


@pytest.mark.sanity
def test_get_single_user(users_api, user_id):
    """Test retrieving a single user"""
    response = users_api.get_user(user_id)
    verify_status_code(response, 200)
    verify_response_key_exists(response, "id")
    data = response.json()
    assert data["id"] == user_id


@pytest.mark.regression
def test_create_user(users_api, user_payload):
    """Test creating a new user"""
    response = users_api.create_user(user_payload)
    verify_status_code(response, 201)
    verify_response_key_exists(response, "id")


@pytest.mark.regression
def test_update_user(users_api, user_id, user_payload):
    """Test updating a user"""
    updated_payload = {**user_payload, "name": "Updated User"}
    response = users_api.update_user(user_id, updated_payload)
    verify_status_code(response, 200)
    data = response.json()
    assert data["name"] == "Updated User"


@pytest.mark.regression
def test_delete_user(users_api, user_id):
    """Test deleting a user"""
    response = users_api.delete_user(user_id)
    verify_status_code(response, 200)
