from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_saucedemo(driver):

    driver.get("https://www.saucedemo.com/")

    # # find elements
    # username_input = driver.find_element(By.ID, "user-name")
    # password_input = driver.find_element(By.ID, "password")
    # login_button = driver.find_element(By.ID, "login-button")

    # interact
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()


    # assertion
    assert "inventory" in driver.current_url

    # driver.quit()
