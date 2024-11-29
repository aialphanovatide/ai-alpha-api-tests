import requests, os
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import requests
from requests import Response

load_dotenv()



class APIClient:
    """
    A API client class for interacting with RESTful APIs using HTTP requests.

    This class supports sending HTTP requests (GET, POST, PUT, DELETE) to a specified base URL.
    The client can be customized with headers, which will be included in all requests.

    Attributes:
        base_url (str): The base URL of the API to which requests will be sent.
        headers (dict[str, str]): Default headers that will be sent with every request.
    """

    def __init__(self, base_url: str, headers: Dict[str, str]) -> None:
        """
        Initializes the APIClient instance with the given base URL and headers.

        Args:
            base_url (str): The base URL of the API.
            headers (dict[str, str]): A dictionary of headers to be included in each request.
        """
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Response:
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint (relative to the base URL).
            params (dict[str, Any], optional): Query parameters to send with the request (default is None).

        Returns:
            requests.Response: The response object from the GET request. Contains status code, content, etc.

        Raises:
            requests.RequestException: If the GET request fails.
            
        """
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=self.headers)

    def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None) -> Response:
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint (relative to the base URL).
            data (dict[str, Any], optional): Data to send with the request (e.g., form data or JSON payload).
            files (dict[str, Any], optional): Files to upload (default is None).

        Returns:
            Response: The response object from the POST request. Contains status code, content, etc.

        Raises:
            requests.RequestException: If the POST request fails.
        """
        return requests.post(f"{self.base_url}{endpoint}", data=data, headers=self.headers, files=files)

    def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, files: Optional[Dict[str, Any]] = None) -> Response:
        """
        Sends a PUT request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint (relative to the base URL).
            data (dict[str, Any], optional): Data to send with the request (e.g., form data or JSON payload).
            files (dict[str, Any], optional): Files to upload (default is None).

        Returns:
            Response: The response object from the PUT request. Contains status code, content, etc.

        Raises:
            requests.RequestException: If the PUT request fails.
        """
        return requests.put(f"{self.base_url}{endpoint}", data=data, headers=self.headers, files=files)

    def delete(self, endpoint: str) -> Response:
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint (relative to the base URL).

        Returns:
            Response: The response object from the DELETE request. Contains status code, content, etc.

        Raises:
            requests.RequestException: If the DELETE request fails.
        """
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)

