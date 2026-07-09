"""Test data samples"""

POST_PAYLOAD = {
    "title": "Test Post",
    "body": "This is a test post",
    "userId": 1
}

POST_UPDATE_PAYLOAD = {
    "title": "Updated Test Post",
    "body": "This is an updated test post",
    "userId": 1
}

INVALID_POST_PAYLOAD = {
    "title": "",
    "body": "",
    "userId": -1
}

USER_PAYLOAD = {
    "name": "Test User",
    "email": "test@example.com",
    "phone": "123-456-7890",
    "website": "example.com"
}

COMMENT_PAYLOAD = {
    "postId": 1,
    "name": "Test Comment",
    "email": "test@example.com",
    "body": "This is a test comment"
}
