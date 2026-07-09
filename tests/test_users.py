import pytest 

@pytest.fixture
def get_info():
    return {
        "me": {
            "name": "Elvin",
            "sex": "male",
            "age": "32"
        },
        "you": {
            "name": "Nika",
            "sex": "female",
            "age": "36"
        }
    }

def test_me_name(get_info):
    updated_info = {**get_info, "you": {
        **get_info["you"],
        "name": "Nazrin"
    }}
    
    assert updated_info["you"]["name"] == "Nazrin"
    
    

