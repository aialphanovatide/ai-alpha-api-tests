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

    Args:
        request: Pytest request fixture used to access parameters passed during the test call.

    Returns:
        APIClient: Configured API client with base URL and headers.
    """

    # Default values for headers
    default_accept = "multipart/form-data"
    default_content_type = None

    # Fetch the parameters if provided in the test, otherwise use defaults
    accept = request.param.get("accept", default_accept) if hasattr(request, 'param') else default_accept
    content_type = request.param.get("content_type", default_content_type) if hasattr(request, 'param') else default_content_type

    base_url = os.getenv("AI_ALPHA_URL")
    api_key = os.getenv("API_KEY")
    
    if not base_url or not api_key:
        raise ValueError("Environment variables 'AI_ALPHA_URL' or 'API_KEY' are missing.")
    
    headers = {
        'accept': accept,
        'X-API-Key': api_key
    }
    if content_type:  # Only include 'Content-Type' if it is provided
        headers['Content-Type'] = content_type
    
    return APIClient(base_url, headers)