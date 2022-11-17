from tests.ui.locators.target_locators import MAIN_PAGE_LOCATORS
from tests.ui.pages.base_page import BasePage, retry
class MainPage(BasePage):

    locators = MAIN_PAGE_LOCATORS()

    @retry
    def logout(self):
        self.click(self.locators.PROFILE_MENU_BUTTON_LOCATOR)
        self.click(self.locators.LOGOUT_BUTTON_LOCATOR)

    @retry
    def change_tab(self, tab_name : str):
        tab_locator = self.locators.TAB_LOCATOR(tab_name)
        self.click(tab_locator)