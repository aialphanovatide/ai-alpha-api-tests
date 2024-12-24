import pytest, os, json
from dotenv import load_dotenv
from utils.api_client import APIClient
from utils.assertions import Assertions
from utils.handlers import Handlers
from test_data.schemas import NEWS_BOTS_SCHEMA, POST_NEWS_BOT_RESPONSE, NEWS_BOT_METRICS_SCHEMA, NEWS_BOT_RESPONSE_SCHEMA

load_dotenv()

@pytest.mark.parametrize(
    "api_client", 
    [{"base_url": os.getenv("NEWS_BOT_URL"), "accept": "application/json"}], 
    indirect=True
)
def test_get_bots(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving all news bots data.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected status code and JSON schema.
    """
    response = api_client.get("bots")
    Assertions.assert_status_code(response, 200)
    Assertions.validate_schema(response.json(), NEWS_BOTS_SCHEMA)

@pytest.mark.parametrize(
    "api_client", 
    [{"base_url": os.getenv("NEWS_BOT_URL"), "content_type": "application/json", "accept": "application/json"}], 
    indirect=True
)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "post_news_bot.json")))
def test_post_bot(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the POST endpoint for creating a new news bot with associated data.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected status code, expected response or JSON schema.
    """
    response = api_client.post("bot", json.dumps(test_data['payload']))
    response_data = response.json()
    Assertions.assert_status_code(response, test_data['status_code'])
    Assertions.validate_schema(response_data, POST_NEWS_BOT_RESPONSE)
    if 'expected_response' in test_data:
        Assertions.assert_response_contains(response_data, eval(test_data['expected_response']))
    api_client.delete(f"bot/{response_data['bot']['id']}") if test_data['status_code'] == 201 else None

@pytest.mark.parametrize(
    "api_client", 
    [{"base_url": os.getenv("NEWS_BOT_URL"), "content_type": "application/json", "accept": "application/json"}], 
    indirect=True
)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "delete_news_bot.json")))
def test_delete_bot(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the DELETE endpoint for deleting a news bot.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected response for the request.

    Raises:
        AssertionError: If the response does not meet the expected status code or response.
    """
    response = api_client.post("bot", json.dumps(test_data['payload']))
    response_data = response.json()
    response = api_client.delete(f"bot/{response_data['bot']['id']}")
    Assertions.assert_status_code(response, test_data['status_code'])
    Assertions.assert_response_contains(response.json(), eval(test_data['expected_response']))

@pytest.mark.parametrize(
    "api_client", 
    [{"base_url": os.getenv("NEWS_BOT_URL"), "content_type": "application/json", "accept": "application/json"}], 
    indirect=True
)
def test_get_news_bot_metrics(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving metrics for a specific bot with pagination and date filtering options.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected status code and JSON schema.
    """
    response = api_client.get("bot/33/metrics")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, NEWS_BOT_METRICS_SCHEMA)

@pytest.mark.parametrize(
    "api_client", 
    [{"base_url": os.getenv("NEWS_BOT_URL"), "content_type": "application/json", "accept": "application/json"}], 
    indirect=True
)
def test_get_bot(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving information for a specific bot, including related keywords, blacklist items, and site data.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected status code and JSON schema.
    """
    response = api_client.get("bot?bot_id=33")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, NEWS_BOT_RESPONSE_SCHEMA)

@pytest.mark.parametrize(
    "api_client", 
    [{"base_url": os.getenv("NEWS_BOT_URL"), "content_type": "application/json", "accept": "application/json"}], 
    indirect=True
)
@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "put_news_bot.json")))
def test_put_news_bot(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the PUT endpoint for updating an existing bot identified by its id. it allows for modification of various bot properties and associated data.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.post("bot", json.dumps({'name': 'catTest','alias': 'CT', 'category_id': '1', 'run_frequency': 20}), [])
    response_data = response.json()
    response1 = api_client.put(f"bot/{response_data['bot']['id']}", json.dumps(test_data['payload'])) 
    response_data1 = response1.json()
    Assertions.assert_status_code(response1, test_data['status_code'])
    test_data['payload']['icon'] = 'https://aialphaicons.s3.us-east-2.amazonaws.com/ct1.svg'
    Assertions.assert_response_contains(response_data1['data'], test_data['payload'])
    api_client.delete(f"bot/{response_data1['data']['id']}") if test_data['status_code'] == 200 else None

    


