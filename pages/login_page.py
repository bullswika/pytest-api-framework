# Jiacheng
# @Time: 2025/12/14
# @Email: bullswika@outlook.com
# @File: login_page.py

from dataclasses import dataclass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@dataclass(frozen=True)
class LoginLocators:
    USERNAME: tuple = (By.ID, "user-name")
    PASSWORD: tuple = (By.ID, "password")
    LOGIN_BTN: tuple = (By.ID, "login-button")
    ERROR: tuple = (By.CSS_SELECTOR, '[data-test="error"]')


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(LoginLocators.USERNAME))
        return self

    def login(self, username: str, password: str):
        self.driver.find_element(*LoginLocators.USERNAME).clear()
        self.driver.find_element(*LoginLocators.USERNAME).send_keys(username)

        self.driver.find_element(*LoginLocators.PASSWORD).clear()
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password)

        self.driver.find_element(*LoginLocators.LOGIN_BTN).click()
        return self

    def is_inventory_page(self) -> bool:
        # 登录成功会跳到 /inventory.html
        return "inventory" in self.driver.current_url

    def get_error_text(self) -> str:
        el = self.wait.until(EC.visibility_of_element_located(LoginLocators.ERROR))
        return el.text.strip()
