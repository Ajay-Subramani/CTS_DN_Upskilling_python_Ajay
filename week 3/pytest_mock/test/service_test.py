from unittest.mock import patch
from service import user_name, post_title

# Mock Database
@patch("service.get_user")
def test_user_name(mock_get_user):
    mock_get_user.return_value = {
        "id": 1,
        "name": "Ajay"
    }

    assert user_name(1) == "Ajay"

# Mock HTTP Request

@patch("api.requests.get")
def test_fetch_post(mock_get):

    mock_response = mock_get.return_value

    mock_response.json.return_value = {
        "id": 1,
        "title": "Mock API Title"
    }

    assert post_title(1) == "Mock API Title"