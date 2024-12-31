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
```

## Project Structure

```
ai-alpha-api-tests/
├── test_data/           # Test data and JSON schemas
│   └── schemas.py       # Contains JSON schemas for response validation
├── tests/              # Test files
│   └── test_category.py # Category API tests
├── utils/              # Utility modules
│   ├── api_client.py   # API client for making HTTP requests
│   └── assertions.py   # Custom assertion methods
├── .env                # Environment variables (create this file)
├── requirements.txt    # Project dependencies
└── README.md
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## Technical Details

- **Python Version**: 3.12
- **Key Dependencies**:
  - pytest 7.2.0 - Testing framework
  - requests 2.31.0 - HTTP client library
  - python-dotenv 1.0.1 - Environment variable management
  - jsonschema 4.23.0 - JSON schema validation

## Schema Validation

The framework includes pre-defined JSON schemas for response validation:
- CATEGORY_SCHEMA - Validates individual category objects
- COIN_SCHEMA - Validates coin objects within categories
- CATEGORIES_RESPONSE_SCHEMA - Validates the complete categories response

## Assertions

Custom assertion methods are available in `utils/assertions.py`:
- `assert_status_code()` - Validates HTTP response status codes
- `validate_schema()` - Validates JSON response against predefined schemas