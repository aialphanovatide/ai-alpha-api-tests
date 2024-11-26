import json, os

class Handlers:

    @staticmethod
    def create_test_tuple(path):
        """
        Reads a JSON file and converts its content into a list of tuples.

        Args:
            path (str): The path to the JSON file containing the test data.

        Returns:
            list[tuple[str, dict]]: A list of tuples. Each tuple contains:
                - A key (str): The test case name or identifier.
                - A value (dict): The corresponding test data (payload, status codes, etc.).

        Raises:
            FileNotFoundError: If the JSON file is not found at the specified path.
            json.JSONDecodeError: If the file content is not valid JSON.
            Exception: For any other unexpected errors during file handling.
        """
        try:
            with open(path, 'r') as jsonFile:
                file = json.load(jsonFile)
            return [(key, value) for key, value in file.items()]
        except FileNotFoundError as e:
            print(f"Error: The file at path '{path}' was not found.")
            raise e
        except json.JSONDecodeError as e:
            print(f"Error: The file at path '{path}' is not a valid JSON file. Details: {e}")
            raise e
        except Exception as e:
            print(f"An unexpected error occurred while processing the file: {e}")
            raise e
        
    @staticmethod
    def file_handler(path, file_name):
        """
        Handles the creation of a file object for upload or further processing.

        Args:
            path (str): The directory path where the file is located.
            file_name (str): The name of the file.

        Returns:
            list: A list containing a tuple with file details for upload.

        Raises:
            FileNotFoundError: If the file does not exist.
            Exception: For any other unexpected errors during file handling.
        """
        try:
            file_path = os.path.join(os.curdir, path, file_name)
            return [('icon', (file_name, open(file_path, 'rb'), 'image/svg+xml'))]
        except FileNotFoundError as e:
            print(f"Error: The file '{file_name}' was not found in path '{path}'.")
            raise e
        except Exception as e:
            print(f"An unexpected error occurred while handling the file: {e}")
            raise e
