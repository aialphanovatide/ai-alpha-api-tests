import pytest, os, json
from dotenv import load_dotenv
from utils.api_client import APIClient
from utils.assertions import Assertions
from utils.handlers import Handlers
from test_data.schemas import NEWS_BOTS_CATEGORIES_SCHEMA, NEWS_BOTS_CATEGORY_SCHEMA, NEWS_BOT_CATEGORY_RESPONSE_SCHEMA

load_dotenv()

def test_get_categories(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving all news bots categories.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.get("categories")
    Assertions.assert_status_code(response, 200)
    Assertions.validate_schema(response.json(), NEWS_BOTS_CATEGORIES_SCHEMA)

@pytest.mark.parametrize("api_client",[{"content_type": "application/json", "accept": "application/json"}], indirect=True)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "post_news_bot_category.json")))
def test_post_category(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the POST endpoint for creating a new news bots category.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected status code or schema.
    """
    response = api_client.post("category", json.dumps(test_data['payload']))
    response_data = response.json()
    Assertions.assert_status_code(response, test_data['status_code'])
    response_data = response.json()
    Assertions.validate_schema(response_data, NEWS_BOT_CATEGORY_RESPONSE_SCHEMA)
    if 'expected_response' in test_data:
        Assertions.assert_response_contains(response_data, eval(test_data['expected_response']))
    api_client.delete(f"category/{response_data['data']['id']}") if test_data['status_code'] == 201 else None

@pytest.mark.parametrize("api_client",[{"content_type": "application/json", "accept": "application/json"}], indirect=True)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "delete_category.json")))
def test_delete_category(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the DELETE endpoint for deleting a news bot category.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected response for the request.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.post("category", json.dumps(test_data['payload']))
    response_data = response.json()
    response = api_client.delete(f"category/{response_data['data']['id']}")
    Assertions.assert_status_code(response, test_data['status_code'])

def test_get_category(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving a specific news bot category by ID.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.get("category?category_name=bitcoin")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, NEWS_BOTS_CATEGORY_SCHEMA)

@pytest.mark.parametrize("api_client",[{"content_type": "application/json", "accept": "multipart/form-data"}], indirect=True)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "put_news_bot_category.json")))
def test_put_category(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the PUT endpoint for updating a news bot category.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.post("category", json.dumps({'name': 'catTest','alias': 'CT'}), [])
    response_data = response.json()
    response1 = api_client.put(f"category/{response_data['data']['id']}", json.dumps(test_data['payload'])) 
    response_data1 = response1.json()
    Assertions.assert_status_code(response1, test_data['status_code'])
    test_data['payload']['icon'] = 'https://aialphaicons.s3.us-east-2.amazonaws.com/ct1.svg'
    Assertions.assert_response_contains(response_data1['data']['category'], test_data['payload'])
    api_client.delete(f"category/{response_data1['data']['category']['id']}") if test_data['status_code'] == 200 else None

    


