# AI ALPHA API Test Automation Framework

This repository contains AI ALPHA API test automation framework built using Python and Pytest. The framework is designed to automate the process of testing RESTful APIs with a focus on maintainability, scalability, and ease of use.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests-locally)
- [Environment Setup](#environment-setup)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## Prerequisites

Before getting started, ensure that you have the following software installed:

- Python 3.12
- pip (Python package installer)
- Virtual environment (optional, but recommended)

## Installation

Follow these steps to set up the framework:

1. Clone the repository:
   ```bash
   git clone https://github.com/aialphanovatide/ai-alpha-api-tests.git
   cd ai-alpha-api-tests
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Mac use 'source venv/bin/activate'
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running tests locally

Once everything is set up, you can run the tests using the following commands:

1. Run all tests:
   ```bash
   pytest
   ```

2. Run tests with detailed output:
   ```bash
   pytest -v
   ```

3. Run tests with print statements output:
   ```bash
   pytest -s
   ```

4. Run a specific test file:
   ```bash
   pytest tests/test_category.py
   ```

5. Run tests matching specific pattern:
   ```bash
   pytest -k "category"
   ```

## Environment Setup

The framework requires certain environment variables to be set. Create a `.env` file in the root directory with the following variables:

```
BASE_URL=<your_api_base_url>
API_KEY=<your_api_key>
NEWS_BOT_URL=<your_news_bot_url>  # Required for news bot tests
```

## Project Structure

```
ai-alpha-api-tests/
├── test_data/           # Test data and JSON schemas
│   ├── schemas.py       # JSON schemas for response validation
│   └── *.json          # Test data files for different endpoints
├── tests/              # Test files
│   ├── conftest.py     # Pytest configuration and fixtures
│   ├── test_category.py # Category API tests
│   ├── test_coin.py    # Coin API tests
│   ├── test_chart.py   # Chart API tests
│   └── test_news_bots_category.py # News bots category tests
├── utils/              # Utility modules
│   ├── api_client.py   # API client for making HTTP requests
│   ├── assertions.py   # Custom assertion methods
│   └── handlers.py     # Helper functions and handlers
├── .env                # Environment variables (create this file)
├── requirements.txt    # Project dependencies
└── README.md
```

## Test Organization

The test suite is organized by API endpoints and functionality:

- **Category Tests**: Basic CRUD operations for categories
- **Coin Tests**: Cryptocurrency-related endpoint testing
- **Chart Tests**: Market data and chart-related endpoints
- **News Bots Tests**: News bot category management

Each test module follows a consistent pattern:
- GET operations
- POST operations
- PUT operations
- DELETE operations

## Test Data Management

Test data is organized in JSON files under the `test_data` directory:
- Schema definitions in `schemas.py`
- Test payloads in separate JSON files per endpoint
- Reusable test data structures

## Assertions and Validations

The framework provides custom assertions through `utils/assertions.py`:
- Status code validation
- Schema validation
- Response content validation
- Custom comparison methods

## Running Tests

Tests can be run by module or functionality:

```bash
# Run all tests
pytest

# Run specific test modules
pytest tests/test_category.py
pytest tests/test_coin.py
pytest tests/test_chart.py
pytest tests/test_news_bots_category.py

# Run tests by pattern
pytest -k "category"  # All category-related tests
pytest -k "get"      # All GET endpoint tests
pytest -k "post"     # All POST endpoint tests
```

## Technical Details

- **Python Version**: 3.12
- **Key Dependencies**:
  - pytest 7.2.0 - Testing framework
  - requests 2.31.0 - HTTP client library
  - python-dotenv 1.0.1 - Environment variable management
  - jsonschema 4.23.0 - JSON schema validation

## Best Practices

1. **Test Independence**: Each test should be independent and self-contained
2. **Clean Up**: Tests should clean up any data they create
3. **Meaningful Names**: Use descriptive test names that indicate the scenario
4. **Documentation**: Maintain docstrings and comments for complex test logic
5. **Schema Validation**: Always validate response schemas for API endpoints

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

