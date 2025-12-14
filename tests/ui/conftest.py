# Jiacheng
# @Time: 2025/12/14
# @Email: bullswika@outlook.com
# @File: conftest.py

import os
from datetime import datetime

import pytest


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False, help="Run browser in headless mode")


@pytest.fixture
def driver(request):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    headless = request.config.getoption("--headless")

    options = Options()
    if headless:
        # 新版 Chrome 推荐的 headless 参数
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,720")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    #save png in artifacts/screenshots/  when fails

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed and "ui" in item.keywords:
        drv = item.funcargs.get("driver")
        if not drv:
            return

        os.makedirs("artifacts/screenshots", exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"artifacts/screenshots/{item.name}_{ts}.png"
        drv.save_screenshot(filename)

        try:
            import allure
            allure.attach.file(filename, name="screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception:
            pass
