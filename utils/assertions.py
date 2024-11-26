from jsonschema import validate, ValidationError

class Assertions:
    @staticmethod
    def assert_status_code(response, expected_status):
        """
        Asserts that the response status code matches the expected status.
        Args:
            response: The response object from the API request.
            expected_status: The expected status code for the API request.
        """
        assert response.status_code == expected_status, (
            f"Expected status {expected_status}, but got {response.status_code}."
        )

    @staticmethod
    def validate_schema(data, schema):
        """
        Validates the given data against a JSON schema.
        """
        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            assert False, f"Schema validation failed: {e.message}"

    @staticmethod
    def assert_response_equals(response, expected_data):
        """
        Asserts that the response JSON equals the expected data.

        Args:
            response: The response object from the API request.
            expected_data: A dictionary containing keys and their expected values.
        """
        assert response.json() == expected_data, (
            f"Response data does not match. Expected: {expected_data}, Got: {response.json()}"
        )

    @staticmethod
    def assert_response_contains(response_data, expected_data):
        """
        Asserts that the response JSON contains specific keys and their expected values.
        
        Args:
            response: The response JSON from the API request.
            expected_data: A dictionary containing keys and their expected values.
        """
        for key, expected_value in expected_data.items():
            assert key in response_data, f"Missing key '{key}' in the response."
            assert response_data[key] == expected_value, (
                f"Key '{key}' has value '{response_data[key]}', "
                f"but expected '{expected_value}'."
            )

