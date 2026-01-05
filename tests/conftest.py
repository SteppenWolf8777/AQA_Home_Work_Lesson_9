import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.driver_name = "chrome"
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 6
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    yield
    browser.quit()