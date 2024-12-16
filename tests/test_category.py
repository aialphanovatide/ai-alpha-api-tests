import pytest, os
from dotenv import load_dotenv
from utils.api_client import APIClient
from utils.assertions import Assertions
from utils.handlers import Handlers
from test_data.schemas import CATEGORIES_RESPONSE_SCHEMA, CATEGORY_RESPONSE_SCHEMA

load_dotenv()

@pytest.fixture(scope="module")
def api_client() -> APIClient:
    """
    Creates and returns an instance of the APIClient with the base URL and API key.

    Returns:
        APIClient: An instance of APIClient configured with base URL and headers.
    """
    return APIClient(os.getenv("AI_ALPHA_URL"), {
            'accept': 'multipart/form-data',
            'X-API-Key': os.getenv("API_KEY")
            })

def test_get_categories(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving all categories.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.get("categories")
    Assertions.assert_status_code(response, 200)
    Assertions.validate_schema(response.json(), CATEGORIES_RESPONSE_SCHEMA)

@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "post_category.json")))
def test_post_category(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the POST endpoint for creating a new category.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected status code or schema.
    """
    response = api_client.post("category", test_data['payload'])
    Assertions.assert_status_code(response, test_data['status_code'])
    response_data = response.json()
    Assertions.validate_schema(response_data, CATEGORY_RESPONSE_SCHEMA)
    if 'expected_response' in test_data:
        Assertions.assert_response_contains(response_data, eval(test_data['expected_response']))
    api_client.delete(f"category/{response_data['category']['category_id']}") if test_data['status_code'] == 201 else None

@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "delete_category.json")))
def test_delete_category(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the DELETE endpoint for deleting a category.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected response for the request.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.post("category", test_data['payload'])
    response_data = response.json()
    response = api_client.delete(f"category/{response_data['category']['category_id']}")
    Assertions.assert_status_code(response, test_data['status_code'])
    Assertions.assert_response_equals(response, eval(test_data['expected_response']))

def test_get_category(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving a specific category by ID.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.get("category/14")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, CATEGORY_RESPONSE_SCHEMA)

@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "put_category.json")))
def test_put_category(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the PUT endpoint for updating a category.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.post("category", {'name': 'catTest','alias': 'CT'}, [])
    response_data = response.json()
    response1 = api_client.put(f"category/{response_data['category']['category_id']}", test_data['payload'], Handlers.file_handler("resources", "test_logo.svg")) 
    response_data1 = response1.json()
    Assertions.assert_status_code(response1, test_data['status_code'])
    test_data['payload']['icon'] = 'https://aialphaicons.s3.us-east-2.amazonaws.com/ct1.svg'
    Assertions.assert_response_contains(response_data1['category'], test_data['payload'])
    api_client.delete(f"category/{response_data1['category']['category_id']}") if test_data['status_code'] == 200 else None

    


