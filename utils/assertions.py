from jsonschema import validate, ValidationError

class Assertions:
    @staticmethod
    def assert_status_code(response, expected_status):
        """
        Asserts that the response status code matches the expected status.
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

