# Jiacheng
# @Time: 2025/12/14
# @Email: bullswika@outlook.com
# @File: test_login_ui.py


import pytest
from pages.login_page import LoginPage


pytestmark = pytest.mark.ui


def test_login_saucedemo_success(driver):
    page = LoginPage(driver).open()
    page.login("standard_user", "secret_sauce")
    assert page.is_inventory_page()


def test_login_saucedemo_invalid_password(driver):
    page = LoginPage(driver).open()
    page.login("standard_user", "wrong_password")
    assert "Username and password do not match" in page.get_error_text()
