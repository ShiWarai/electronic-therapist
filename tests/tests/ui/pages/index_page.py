from tests.ui.locators.target_locators import INDEX_PAGE_LOCATORS
from tests.ui.pages.base_page import BasePage, retry


class IndexPage(BasePage):
    locators = INDEX_PAGE_LOCATORS()
