import pytest
from selene import browser


@pytest.fixture()
def manage_browser():
    browser.config.window_height = 800
    browser.config.window_width = 800
    browser.config.base_url = "https://www.google.com"

    yield
    browser.quit()