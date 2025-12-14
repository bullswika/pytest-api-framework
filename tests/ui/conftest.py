# Jiacheng
# @Time: 2025/12/14
# @Email: bullswika@outlook.com
# @File: conftest.py

import os
from datetime import datetime
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()

    # CI-friendly headless mode
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):


    outcome = yield
    report = outcome.get_result()

    # Only care about the actual test execution ("call"), not setup/teardown
    if report.when != "call":
        return

    if report.failed:
        driver = item.funcargs.get("driver")
        if not driver:
            return
        #artifacts/screenshots
        screenshots_dir = Path("artifacts") / "screenshots"
        screenshots_dir.mkdir(parents=True, exist_ok=True)

        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Make a safe filename
        safe_name = item.nodeid.replace("/", "_").replace("::", "__").replace("\\", "_")
        filename = screenshots_dir / f"{safe_name}_{ts}.png"

        driver.save_screenshot(str(filename))
