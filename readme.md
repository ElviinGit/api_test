# API Testing Framework

A comprehensive Python API testing framework built with pytest and requests for testing REST APIs.

## 📖 Overview

This framework provides a clean, modular, and reusable approach to API testing. It covers CRUD operations, various assertion patterns, environment-specific configurations, and best practices for test organization.

## 🎯 Objectives

✅ Clean, reusable test framework with pytest  
✅ Support for multiple environments (QA, Stage, Prod)  
✅ Comprehensive assertions for API responses  
✅ Modular API client classes  
✅ Proper logging and reporting  
✅ Easy to extend and maintain  

## 🛠 Tech Stack

- **Python 3.x** - Programming language
- **pytest** - Test runner and framework
- **requests** - HTTP client library
- **pytest-html** - HTML reporting
- **pytest-cov** - Code coverage reporting

## 📁 Project Structure

```
apitest/
├── api/
│   ├── base_api.py          # Base API class with HTTP methods
│   ├── post_api.py          # Posts API endpoints
│   ├── users_api.py         # Users API endpoints
│   └── users_api.py         # Comments API endpoints
├── config/
│   ├── config.py            # Configuration manager
│   ├── qa.json              # QA environment config
│   ├── stage.json           # Stage environment config
│   └── prod.json            # Prod environment config
├── data/
│   └── test_data.py         # Test data samples
├── tests/
│   ├── test_posts.py        # Post API tests
│   ├── test_users.py        # User API tests
│   └── test_comments.py     # Comments API tests
├── utils/
│   ├── assertions.py        # Custom assertion functions
│   └── logger.py            # Logging configuration
├── logs/                    # Test logs directory
├── conftest.py              # Pytest fixtures
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
└── readme.md                # This file
```

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Tests

**Run all tests:**
```bash
pytest
```

**Run specific test file:**
```bash
pytest tests/test_posts.py
```

**Run tests with specific marker:**
```bash
pytest -m smoke
pytest -m sanity
pytest -m regression
```

**Run with verbose output:**
```bash
pytest -v
```

**Run with HTML report:**
```bash
pytest --html=report.html
```

**Run with coverage report:**
```bash
pytest --cov=api --cov=utils
```

### 3. Run Tests in Specific Environment

```bash
# Set environment variable before running tests
set TEST_ENV=qa
pytest

# Or specify in command
pytest -m smoke --TEST_ENV=prod
```

## 📝 Writing Tests

### Basic Test Example

```python
from utils.assertions import verify_status_code, verify_response_key_exists

def test_create_post(post_api, post_payload):
    """Test creating a new post"""
    response = post_api.create_post(post_payload)
    verify_status_code(response, 201)
    verify_response_key_exists(response, "id")
```

### Using Markers

```python
@pytest.mark.smoke
def test_get_posts(post_api):
    response = post_api.get_posts()
    verify_status_code(response, 200)

@pytest.mark.sanity
def test_create_post(post_api, post_payload):
    response = post_api.create_post(post_payload)
    verify_status_code(response, 201)

@pytest.mark.regression
def test_update_post(post_api, post_id, post_payload):
    response = post_api.update_post(post_id, post_payload)
    verify_status_code(response, 200)
```

## 🔧 API Classes

### PostApi

Methods for Posts endpoints:
- `get_posts()` - Get all posts
- `create_post(payload)` - Create a post
- `update_post(post_id, payload)` - Update a post
- `delete_post(post_id)` - Delete a post

### UsersApi

Methods for Users endpoints:
- `get_users()` - Get all users
- `get_user(user_id)` - Get a specific user
- `create_user(payload)` - Create a user
- `update_user(user_id, payload)` - Update a user
- `delete_user(user_id)` - Delete a user

### CommentsApi

Methods for Comments endpoints:
- `get_comments()` - Get all comments
- `get_comment(comment_id)` - Get a specific comment
- `get_post_comments(post_id)` - Get comments for a post
- `create_comment(payload)` - Create a comment
- `update_comment(comment_id, payload)` - Update a comment
- `delete_comment(comment_id)` - Delete a comment

## ✅ Available Assertions

### verify_status_code(response, expected)
```python
verify_status_code(response, 200)
```

### verify_response_key_exists(response, key)
```python
verify_response_key_exists(response, "id")
```

### verify_response_contains(response, expected_dict)
```python
verify_response_contains(response, {"title": "Test", "userId": 1})
```

### verify_response_type(response, expected_type)
```python
verify_response_type(response, list)
```

### verify_array_not_empty(response)
```python
verify_array_not_empty(response)
```

### verify_array_contains_key(response, key)
```python
verify_array_contains_key(response, "id")
```

## 📊 Configuration

Environment configurations are managed in `config/` directory:

### qa.json
```json
{
  "base_url": "https://jsonplaceholder.typicode.com",
  "timeout": 10,
  "retry_attempts": 3,
  "log_level": "INFO"
}
```

Modify these files to point to your API endpoints in different environments.

## 📋 Test Markers

- `@pytest.mark.smoke` - Quick smoke tests
- `@pytest.mark.sanity` - Sanity/functional tests
- `@pytest.mark.regression` - Regression tests

## 📝 Fixtures

Available pytest fixtures defined in `conftest.py`:

- `post_api` - PostApi instance
- `post_payload` - Sample post data
- `post_id` - Sample post ID
- `users_api` - UsersApi instance
- `user_payload` - Sample user data
- `user_id` - Sample user ID
- `comments_api` - CommentsApi instance
- `comment_payload` - Sample comment data
- `comment_id` - Sample comment ID

## 🔍 Logging

All API requests are logged to `logs/api.log` with:
- Request method (GET, POST, PUT, DELETE)
- Request URL
- Request payload (for POST/PUT requests)
- Timestamp and log level

## 📈 Next Steps

To extend the framework:

1. **Add New API Endpoints**: Create new classes extending `BaseApi`
2. **Add More Assertions**: Extend `utils/assertions.py`
3. **Add Test Data**: Extend `data/test_data.py`
4. **Add Environment Configs**: Extend config JSON files
5. **Add Custom Fixtures**: Extend `conftest.py`

## 📞 Support

For issues or questions, please refer to the pytest documentation or the inline code comments.
