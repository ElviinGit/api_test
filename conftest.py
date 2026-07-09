import pytest
from api.post_api import PostApi
from api.users_api import UsersApi, CommentsApi
from data.test_data import POST_PAYLOAD, USER_PAYLOAD, COMMENT_PAYLOAD

# Post API fixtures
@pytest.fixture
def post_api():
    """Fixture for PostApi"""
    return PostApi()

@pytest.fixture
def post_payload():
    """Fixture for post payload"""
    return POST_PAYLOAD.copy()

@pytest.fixture
def post_id():
    """Fixture for post ID"""
    return 1

# User API fixtures
@pytest.fixture
def users_api():
    """Fixture for UsersApi"""
    return UsersApi()

@pytest.fixture
def user_payload():
    """Fixture for user payload"""
    return USER_PAYLOAD.copy()

@pytest.fixture
def user_id():
    """Fixture for user ID"""
    return 1

# Comments API fixtures
@pytest.fixture
def comments_api():
    """Fixture for CommentsApi"""
    return CommentsApi()

@pytest.fixture
def comment_payload():
    """Fixture for comment payload"""
    return COMMENT_PAYLOAD.copy()

@pytest.fixture
def comment_id():
    """Fixture for comment ID"""
    return 1
