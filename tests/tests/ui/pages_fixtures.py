import pytest

from tests.ui.pages.main_page import MainPage

@pytest.fixture
def main_page(driver):
    return MainPage(driver)