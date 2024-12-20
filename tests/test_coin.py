import pytest, os
from utils.api_client import APIClient
from utils.assertions import Assertions
from utils.handlers import Handlers
from test_data.schemas import *

def test_get_coins(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving all coins.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.get("coins")
    Assertions.assert_status_code(response, 200)
    Assertions.validate_schema(response.json(), COINS_RESPONSE_SCHEMA)

@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "post_coin.json")))
def test_post_coin(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the POST endpoint for creating a new coin.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected status code or schema.
    """
    response = api_client.post("coin", test_data['payload'])
    Assertions.assert_status_code(response, test_data['status_code'])
    response_data = response.json()
    Assertions.validate_schema(response_data, COIN_RESPONSE_SCHEMA)
    if 'expected_response' in test_data:
        Assertions.assert_response_contains(response_data, eval(test_data['expected_response']))
    api_client.delete(f"coin/{response_data['coin']['bot_id']}") if test_data['status_code'] == 201 else None

@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "delete_coin.json")))
def test_delete_coin(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the DELETE endpoint for deleting a coin.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected response for the request.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.post("coin", test_data['payload'])
    response_data = response.json()
    response = api_client.delete(f"coin/{response_data['coin']['bot_id']}")
    Assertions.assert_status_code(response, test_data['status_code'])
    Assertions.assert_response_equals(response, eval(test_data['expected_response']))

def test_get_coin(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving a specific coin by ID.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.get("coin/14")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, COIN_RESPONSE_SCHEMA)

@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "put_coin.json")))
def test_put_coin(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the PUT endpoint for updating a coin.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.post("coin", {'name': 'coinTest','alias': 'CT',"symbol": "ct","category_id": 1}, [])
    response_data = response.json()
    response1 = api_client.put(f"coin/{response_data['coin']['bot_id']}", test_data['payload'], Handlers.file_handler("resources", "test_logo.svg")) 
    response_data1 = response1.json()
    Assertions.assert_status_code(response1, test_data['status_code'])
    test_data['payload']['icon'] = 'https://aialphaicons.s3.us-east-2.amazonaws.com/ct1.svg'
    Assertions.assert_response_contains(response_data1['coin'], test_data['payload'])
    api_client.delete(f"coin/{response_data1['coin']['bot_id']}") if test_data['status_code'] == 200 else None

    


