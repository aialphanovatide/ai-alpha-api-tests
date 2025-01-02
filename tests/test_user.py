import pytest, os, json
from dotenv import load_dotenv
from utils.api_client import APIClient
from utils.assertions import Assertions
from utils.handlers import Handlers
from test_data.schemas import USERS_SCHEMA, USER_SCHEMA, USER_RESPONSE_SCHEMA


def test_get_users(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving all users with their purchased plans, with optional pagination.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected status code and JSON schema.
    """
    response = api_client.get("users")
    Assertions.assert_status_code(response, 200)
    Assertions.validate_schema(response.json(), USERS_SCHEMA)

@pytest.mark.parametrize(
    "api_client", 
    [{"accept": "application/json",
      "content_type": "application/json"}], 
    indirect=True
)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "post_user.json")))
def test_post_user(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the POST endpoint for registering a new user with associated data in the system.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected status code, expected response or JSON schema.
    """
    response = api_client.post("user", json.dumps(test_data['payload']))
    response_data = response.json()
    Assertions.assert_status_code(response, test_data['status_code'])
    Assertions.validate_schema(response_data, USER_SCHEMA)
    if 'expected_response' in test_data:
        Assertions.assert_response_contains(response_data, test_data['expected_response'])
    api_client.delete(f"user", json.dumps({ "email": "testpost@gmail.com"})) if test_data['status_code'] == 201 else None

@pytest.mark.parametrize(
    "api_client", 
    [{"content_type": "application/json", "accept": "application/json"}], 
    indirect=True
)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "delete_user.json")))
def test_delete_user(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the DELETE endpoint for deleting a user identified by auth0id or email.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected response for the request.

    Raises:
        AssertionError: If the response does not meet the expected status code or response.
    """
    response = api_client.post("user", json.dumps({"email": "felicitasperedo@gmail.com", "full_name": "felicitas pe", "nickname": "testuser" }))
    response = api_client.delete("user", json.dumps({ "email": "felicitasperedo@gmail.com"}))
    Assertions.assert_status_code(response, test_data['status_code'])
    Assertions.assert_response_contains(response.json(), eval(test_data['expected_response']))

@pytest.mark.parametrize(
    "api_client", 
    [{"content_type": "application/json", "accept": "application/json"}], 
    indirect=True
)
def test_get_user(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving a specific user with their purchased plans.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected status code and JSON schema.
    """
    response = api_client.get("user?email=ferlymirza11@gmail.com")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, USER_RESPONSE_SCHEMA)

@pytest.mark.parametrize(
    "api_client", 
    [{"content_type": "application/json", "accept": "application/json"}], 
    indirect=True
)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "put_user.json")))
def test_put_user(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the PUT endpoint for updating an existing user identified by it's id. It allows for modification of various properties and associated data.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.post("user", json.dumps({"email": "felicitasperedo97+6@gmail.com", "full_name": "felicitas pe", "nickname": "felip123456" }), [])
    response_data = response.json()
    response1 = api_client.put(f"user/{response_data['user']['user_id']}", json.dumps(test_data['payload'])) 
    response_data1 = response1.json()
    Assertions.assert_status_code(response1, test_data['status_code'])
    Assertions.assert_response_contains(response_data1['data'], test_data['payload'])
    api_client.delete(f"user", json.dumps({ "email": "felicitasperedo97+6@gmail.com"})) if test_data['status_code'] == 200 else None

    


