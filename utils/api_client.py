import requests, os
from dotenv import load_dotenv

load_dotenv()

import requests

class APIClient:
    """
    A API client class for interacting with RESTful APIs using HTTP requests.

    This class supports sending HTTP requests (GET, POST, PUT, DELETE) to a specified base URL.
    The client can be customized with headers, which will be included in all requests.

    Attributes:
        base_url (str): The base URL of the API to which requests will be sent.
        headers (dict): Default headers that will be sent with every request.
    """

    def __init__(self, base_url, headers):
        """
        Initializes the APIClient instance with the given base URL and headers.

        Args:
            base_url (str): The base URL of the API (e.g., 'https://api.example.com').
            headers (dict): A dictionary of headers to be included in each request (e.g., {'Authorization': 'Bearer token'}).
        """
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint, params=None):
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint (relative to the base URL).
            params (dict, optional): Query parameters to send with the request (default is None).

        Returns:
            requests.Response: The response object from the GET request. Contains status code, content, etc.
            
        """
        return requests.get(f"{self.base_url}{endpoint}", params=params, headers=self.headers)

    def post(self, endpoint, data=None, files=None):
        """
        Sends a POST request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint (relative to the base URL).
            data (dict, optional): Data to send with the request (e.g., form data or JSON payload).
            files (dict, optional): Files to upload (default is None).

        Returns:
            requests.Response: The response object from the POST request. Contains status code, content, etc.

        """
        return requests.post(f"{self.base_url}{endpoint}", data=data, headers=self.headers, files=files)

    def put(self, endpoint, data=None, files=None):
        """
        Sends a PUT request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint (relative to the base URL).
            data (dict, optional): Data to send with the request (e.g., form data or JSON payload).
            files (dict, optional): Files to upload (default is None).

        Returns:
            requests.Response: The response object from the PUT request. Contains status code, content, etc.

        """
        return requests.put(f"{self.base_url}{endpoint}", data=data, headers=self.headers, files=files)

    def delete(self, endpoint):
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint (relative to the base URL).

        Returns:
            requests.Response: The response object from the DELETE request. Contains status code, content, etc.

        """
        return requests.delete(f"{self.base_url}{endpoint}", headers=self.headers)

