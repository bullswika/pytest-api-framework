# Jiacheng
# @Time: 2025/12/11
# @Email: bullswika@outlook.com
# @File: conftest.py

import pytest
from common.config import BASE_URL
from common.api_client import APIClient
import logging
from selenium import webdriver


def pytest_configure():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

@pytest.fixture(scope="session")
def base_url():
    print(">>>setup base_url =", BASE_URL)
    return BASE_URL

@pytest.fixture(scope="session")
def token(base_url):
    fake_token = "global_token-xyz"
    print(f">>>setup token using base_url={base_url}, token={fake_token}")
    return fake_token

@pytest.fixture(scope="session")
def api_client(base_url, token):
    client = APIClient(base_url=base_url, token=token)
    print(">>>setup api_client")
    return client


