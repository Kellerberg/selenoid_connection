import os
import pytest
from selene import Config
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)
    Config.browser_name = 'chrome'
    Config.timeout = 10
    Config.driver = driver
    yield driver
    driver.quit()
