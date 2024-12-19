import os
from dotenv import load_dotenv
import pytest
from utils.api_client import APIClient

# Load environment variables
load_dotenv()

@pytest.fixture(scope="module")
def api_client(request) -> APIClient:
    """
    Provides a configured APIClient instance for use in tests, with parameters passed to it.

    This fixture supports customization of the API client configuration by allowing test cases 
    to provide the following parameters via `request.param`:
    
    - `base_url` (str): The base URL for the API. Defaults to the `AI_ALPHA_URL` environment variable.
    - `accept` (str): The value for the `accept` header. Defaults to "multipart/form-data".
    - `content_type` (str): The value for the `Content-Type` header. Defaults to None (header not included).

    Environment variables:
    - `AI_ALPHA_URL`: Used as the default value for `base_url` if not provided via `request.param`.
    - `API_KEY`: Required for the `X-API-Key` header.

    Args:
        request: Pytest request fixture used to access parameters passed during the test call.

    Returns:
        APIClient: Configured API client with the specified base URL and headers.

    Raises:
        ValueError: If the `AI_ALPHA_URL` or `API_KEY` environment variable is missing, or if `base_url`
                    is not provided via parameters or environment variable.
    """
    # Default values for headers
    default_accept = "multipart/form-data"
    default_content_type = None

    # Fetch the parameters if provided in the test, otherwise use defaults
    base_url = request.param.get("base_url", os.getenv("AI_ALPHA_URL")) if hasattr(request, 'param') else os.getenv("AI_ALPHA_URL")
    accept = request.param.get("accept", default_accept) if hasattr(request, 'param') else default_accept
    content_type = request.param.get("content_type", default_content_type) if hasattr(request, 'param') else default_content_type
    
    if not base_url:
        raise ValueError("Base URL is required. Provide 'base_url' as a parameter or set the 'AI_ALPHA_URL' environment variable.")

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("Environment variable 'API_KEY' is missing.")
    
    headers = {
        'accept': accept,
        'X-API-Key': api_key
    }
    if content_type:  # Only include 'Content-Type' if it is provided
        headers['Content-Type'] = content_type
    
    return APIClient(base_url, headers)