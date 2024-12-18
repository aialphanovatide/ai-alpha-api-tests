import pytest, os, json
from dotenv import load_dotenv
from utils.api_client import APIClient
from utils.assertions import Assertions
from utils.handlers import Handlers
from test_data.schemas import CHART_RESPONSE_SCHEMA, TOP_MOVERS_SCHEMA, OHLC_CHART_SCHEMA, CHART_GET_SCHEMA

load_dotenv()

@pytest.fixture(scope="module")
def api_client() -> APIClient:
    """
    Creates and returns an instance of the APIClient with the base URL and API key for use in tests.

    Returns:
        APIClient: An instance of APIClient configured with base URL and headers.
    """
    
    return APIClient(os.getenv("AI_ALPHA_URL"), {
            'accept': 'application/json',
            'Content-Type': 'application/json',
            'X-API-Key': os.getenv("API_KEY")
            })


@pytest.mark.parametrize("test_name, test_data", Handlers.create_test_tuple(os.path.join(os.curdir, "test_data", "post_chart.json")))
def test_post_chart(api_client: APIClient, test_name: str, test_data: dict) -> None:
    """
    Tests the POST endpoint for creating a new chart.

    Args:
        api_client (APIClient): The API client used for making requests.
        test_name (str): The name of the test case.
        test_data (dict): The payload and expected status code for the request.

    Raises:
        AssertionError: If the response does not meet the expected status code or schema.
    """
    response = api_client.post("chart", json.dumps(test_data['payload']))
    response_data = response.json()
    Assertions.assert_status_code(response, test_data['status_code'])
    response_data = response.json()
    Assertions.validate_schema(response_data, CHART_RESPONSE_SCHEMA)
    if 'expected_response' in test_data:
        Assertions.assert_response_contains(response_data, eval(test_data['expected_response']))
    api_client.delete(f"chart/{response_data['data']['chart_id']}") if test_data['status_code'] == 201 else None


def test_get_chart(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving a specific chart by ID.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected conditions.
    """
    response = api_client.get(f"chart?coin_name=&coin_id=1&temporality=1d&pair=usdt")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, CHART_GET_SCHEMA)

def test_get_total3_chart(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving a total3 chart by days.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected status code or schema.
    """
    response = api_client.get("chart/total3?days=1")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, CHART_RESPONSE_SCHEMA)

def test_get_top_movers(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving a top movers.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected status code or schema.
    """
    response = api_client.get("chart/top-movers")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, TOP_MOVERS_SCHEMA)

def test_get_ohlc_chart(api_client: APIClient) -> None:
    """
    Tests the GET endpoint for retrieving a OHLC Chart.

    Args:
        api_client (APIClient): The API client used for making requests.

    Raises:
        AssertionError: If the response does not meet the expected status code or schema.
    """
    response = api_client.get("chart/ohlc?gecko_id=1&vs_currency=usd&interval=1d&precision=2&symbol=BTC")
    Assertions.assert_status_code(response, 200)
    response_data = response.json()
    Assertions.validate_schema(response_data, OHLC_CHART_SCHEMA)
