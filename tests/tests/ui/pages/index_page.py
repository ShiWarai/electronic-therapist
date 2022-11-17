from tests.ui.locators.target_locators import INDEX_PAGE_LOCATORS
from tests.ui.pages.base_page import BasePage


class IndexPage(BasePage):
    locators = INDEX_PAGE_LOCATORS

    def start_new_examination(self) -> bool:
        if self.is_find(self.locators.START_BUTTON_LOCATOR):
            self.click(self.locators.START_BUTTON_LOCATOR)
        else:
            raise Exception("No such button!")

    def next_question(self) -> tuple:

        last = self.find_visible(self.locators.TEXT_QUESTION_LOCATOR).text

        self.click(self.locators.NEXT_BUTTON_LOCATOR)

        new = self.find_visible(self.locators.TEXT_QUESTION_LOCATOR).text

        return (last, new)
