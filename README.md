# Pytest API & UI Automation Framework

A practical test automation framework built with **Python** and **Pytest**, supporting both **REST API testing** and **Selenium UI testing**, with **GitHub Actions CI integration**.

This project focuses on clean structure, maintainability, and realistic CI execution strategies.

---

## Tech Stack

- **Language**: Python 3.11
- **Test Framework**: Pytest
- **API Testing**: Requests
- **UI Testing**: Selenium WebDriver
- **CI/CD**: GitHub Actions

---

## Project Structure

```text
common/
  api_client.py        # Reusable HTTP client wrapper
  config.py            # Global configuration

pages/
  login_page.py        # Page Object Model (POM) for login page

tests/
  conftest.py          # API-level shared fixtures
  api/
    test_user_api.py   # User API test cases
    test_posts_api.py  # Posts API test cases
  ui/
    conftest.py        # Selenium WebDriver fixtures
    test_login_ui.py   # UI login automation test

.github/
  workflows/
    pytest.yaml        # CI workflow configuration

pytest.ini
requirements.txt
README.md
```

---

## Features

### API Automation
- REST API testing using **pytest + requests**
- API client abstraction for reusable request handling
- Test categorization using pytest markers: `smoke`, `regression`
- Parameterized test cases
- Shared fixtures using `conftest.py`

### UI Automation
- Selenium-based UI automation for login flow
- **Page Object Model (POM)** to separate test logic from page interactions
- WebDriver lifecycle managed via Pytest fixtures
- Headless browser support for CI environments
- Automatic screenshot capture on test failure

### CI Integration
- GitHub Actions used for continuous integration
- **API tests** run automatically on every push and pull request
- **UI tests** run manually using `workflow_dispatch` to avoid flaky UI failures affecting regular CI runs

---

## How to Run Tests Locally

### 1) Install dependencies

```bash
pip install -r requirements.txt
```

### 2) Run all API tests

```bash
pytest tests/api -v
```

### 3) Run smoke tests only

```bash
pytest -m smoke
```

### 4) Run UI tests

```bash
pytest tests/ui -v
```

### 5) Run UI tests in headless mode

```bash
pytest tests/ui -v --headless
```

---

## CI Strategy

- API tests run automatically on every push and pull request
- UI tests are triggered manually via `workflow_dispatch`
- UI tests run in headless mode inside CI
- API and UI tests are isolated to avoid Selenium dependency issues

---

## Author

Jiacheng    
GitHub: https://github.com/bullswika
