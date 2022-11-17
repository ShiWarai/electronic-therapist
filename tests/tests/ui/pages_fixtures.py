import pytest

from tests.ui.pages.index_page import IndexPage


@pytest.fixture
def index_page(driver, config, logger):
    return IndexPage(driver, config, logger)
