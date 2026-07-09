def verify_status_code(response, expected):
    """Verify response status code"""
    assert response.status_code == expected, f"Expected {expected}, got {response.status_code}"

def verify_response_key_exists(response, key):
    """Verify a key exists in response JSON"""
    data = response.json()
    assert key in data, f"Key '{key}' not found in response: {data}"

def verify_response_contains(response, expected_dict):
    """Verify response contains expected key-value pairs"""
    data = response.json()
    for key, value in expected_dict.items():
        assert key in data, f"Key '{key}' not found in response"
        assert data[key] == value, f"Expected {key}={value}, got {key}={data[key]}"

def verify_response_type(response, expected_type):
    """Verify response JSON is of expected type (list, dict, etc)"""
    data = response.json()
    assert isinstance(data, expected_type), f"Expected {expected_type}, got {type(data)}"

def verify_array_not_empty(response):
    """Verify response is a non-empty array"""
    data = response.json()
    assert isinstance(data, list), f"Expected list, got {type(data)}"
    assert len(data) > 0, "Expected non-empty array"

def verify_array_contains_key(response, key):
    """Verify all items in response array contain a specific key"""
    data = response.json()
    assert isinstance(data, list), f"Expected list, got {type(data)}"
    for item in data:
        assert key in item, f"Key '{key}' not found in array item: {item}"
