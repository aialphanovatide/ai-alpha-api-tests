import pytest, os
from dotenv import load_dotenv
from utils.api_client import APIClient
from utils.assertions import Assertions
from test_data.schemas import CATEGORIES_RESPONSE_SCHEMA

load_dotenv()

@pytest.fixture(scope="module")
def api_client():
    return APIClient(os.getenv("BASE_URL"), {
            'accept': 'application/json',
            'X-API-Key': os.getenv("API_KEY")
            })

def test_get_categories(api_client):
    response = api_client.get("categories")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, CATEGORIES_RESPONSE_SCHEMA)
