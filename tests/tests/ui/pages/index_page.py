from typing import Callable

from selenium.common.exceptions import TimeoutException

from tests.ui.locators.target_locators import INDEX_PAGE_LOCATORS
from tests.ui.pages.base_page import BasePage


class NoSuchButtonException(Exception):
    pass


class IndexPage(BasePage):
    locators = INDEX_PAGE_LOCATORS

    def start_new_examination(self) -> bool:
        if self.is_find(self.locators.START_BUTTON_LOCATOR):
            self.click(self.locators.START_BUTTON_LOCATOR)
        else:
            raise self.NoSuchButtonException()

    def choose_any_answer(self, answer_text):
        try:
            if not self.__is_text_question():
                self.find_all(self.locators.ANSWERS_BUTTONS_LOCATOR)[1].click()
            else:
                self.find_visible(self.locators.ANSWER_TEXTAREA_LOCATOR).send_keys(answer_text)
        except TimeoutException:
            raise self.NoSuchButtonException()

    def next_question(self) -> tuple:
        last = self.find_visible(self.locators.TEXT_QUESTION_LOCATOR).text

        self.click(self.locators.NEXT_BUTTON_LOCATOR)

        try:
            new = self.find_visible(self.locators.TEXT_QUESTION_LOCATOR).text
        except TimeoutException:
            self.find_visible(self.locators.RESULT_TITLE_LOCATOR)
            new = None

        return (last, new)

    def pass_examination(self, answer_question_func: Callable) -> bool:
        self.start_new_examination()

        while True:
            try:
                question = self.find_visible(self.locators.TEXT_QUESTION_LOCATOR).text
                answer = answer_question_func(question)

                if self.__is_text_question():
                    self.find_visible(self.locators.ANSWER_TEXTAREA_LOCATOR).send_keys(answer)
                else:
                    self.click(self.locators.ANSWER_BUTTON_LOCATOR(answer))

                self.next_question()
                continue
            except TimeoutException:
                break

        return True

    def __is_text_question(self) -> bool:
        try:
            self.find_all(self.locators.ANSWERS_BUTTONS_LOCATOR)
            return False
        except TimeoutException:
            self.find_visible(self.locators.ANSWER_TEXTAREA_LOCATOR)
            return True
