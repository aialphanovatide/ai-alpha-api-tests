from jsonschema import validate, ValidationError
from requests import Response
from typing import Any, Dict

class Assertions:
    """
    A utility class for performing various assertions on API responses and data validation.

    This class includes methods for asserting HTTP status codes, validating JSON schemas,
    and checking the contents of API responses.
    """

    @staticmethod
    def assert_status_code(response: Response, expected_status: int) -> None:
        """
        Asserts that the response status code matches the expected status.
        
        Args:
            response (Response): The response object from the API request.
            expected_status (int): The expected status code for the API request.

        Raises:
            AssertionError: If the response status code does not match the expected status.
        """
        assert response.status_code == expected_status, (
            f"Expected status {expected_status}, but got {response.status_code}."
        )

    @staticmethod
    def validate_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> None:
        """
        Validates the given data against a JSON schema.

        Args:
            data (dict[str, Any]): The JSON data to be validated.
            schema (dict[str, Any]): The JSON schema to validate against.

        Raises:
            AssertionError: If validation fails, an assertion error is raised with the error message.
        """
        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            assert False, f"Schema validation failed: {e.message}"

    @staticmethod
    def assert_response_equals(response: Response, expected_data: Dict[str, Any]) -> None:
        """
        Asserts that the response JSON equals the expected data.

        Args:
            response (Response): The response object from the API request.
            expected_data (dict[str, Any]): A dictionary containing keys and their expected values.

        Raises:
            AssertionError: If the response JSON does not exactly match the expected data.
        """
        assert response.json() == expected_data, (
            f"Response data does not match. Expected: {expected_data}, Got: {response.json()}"
        )

    @staticmethod
    def assert_response_contains(response_data: Dict[str, Any], expected_data: Dict[str, Any]) -> None:
        """
        Asserts that the response JSON contains specific keys and their expected values.

        Args:
            response (dict[str, Any]): The response json from the API request.
            expected_data (dict[str, Any]): A dictionary containing keys and their expected values.

        Raises:
            AssertionError: If the response JSON does not contain the expected keys and values.
        """
        for key, expected_value in expected_data.items():
            assert key in response_data, f"Missing key '{key}' in the response."
            assert response_data[key] == expected_value, (
                f"Key '{key}' has value '{response_data[key]}', "
                f"but expected '{expected_value}'."
            )

