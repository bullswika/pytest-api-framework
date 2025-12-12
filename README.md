# Pytest API Automation Framework

A lightweight API automation testing framework built with **Python**, **pytest**, and **requests**.

## Tech Stack
- Python 3
- pytest
- requests

## Project Structure

```
common/
    api_client.py         # HTTP client wrapper
    config.py             # Global configuration

tests/
    api/
        test_posts_api.py
    conftest.py           # Shared fixtures

pytest.ini
```


## Features
- Pytest fixtures with session scope
- API client abstraction
- Parametrized test cases
- Test categorization with pytest markers (smoke, regression)
- Easy integration with CI tools

## How to Run Tests

```bash
pip install -r requirements.txt
pytest -v
```

##  Run smoke tests only:
pytest -m smoke
