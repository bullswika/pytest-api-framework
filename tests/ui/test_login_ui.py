# Jiacheng
# @Time: 2025/12/14
# @Email: bullswika@outlook.com
# @File: test_login_ui.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

pytestmark = pytest.mark.ui

@pytest.mark.smoke
def test_login_saucedemo_success(driver):
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    # Wait until username input is visible
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Assert we navigated to the inventory page
    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url
    # assert False