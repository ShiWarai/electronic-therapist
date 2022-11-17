from selenium.common.exceptions import TimeoutException

from tests.ui.locators.target_locators import INDEX_PAGE_LOCATORS
from tests.ui.pages.base_page import BasePage


class IndexPage(BasePage):
    locators = INDEX_PAGE_LOCATORS

    def start_new_examination(self) -> bool:
        if self.is_find(self.locators.START_BUTTON_LOCATOR):
            self.click(self.locators.START_BUTTON_LOCATOR)
        else:
            raise Exception("No such button!")

    def choose_any_answer(self, answer_text):
        try:
            try:
                self.find_all(self.locators.ANSWERS_BUTTONS_LOCATOR)[1].click()
            except TimeoutException:
                self.find_visible(self.locators.ANSWER_TEXTAREA_LOCATOR).send_keys(answer_text)
        except TimeoutException:
            raise Exception("No such button!")



    def next_question(self) -> tuple:
        last = self.find_visible(self.locators.TEXT_QUESTION_LOCATOR).text

        self.click(self.locators.NEXT_BUTTON_LOCATOR)

        try:
            new = self.find_visible(self.locators.TEXT_QUESTION_LOCATOR).text
        except TimeoutException:
            self.find_visible(self.locators.RESULT_TITLE_LOCATOR)
            new = None

        return (last, new)
