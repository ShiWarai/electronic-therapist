from urllib.parse import urlparse

import selenium.common.exceptions
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils.decorators import retry, wait

from tests.ui.locators.target_locators import BASE_PAGE_LOCATORS

N_RETRIES = 3
BASE_DELAY = 1


class BasePage:
    locators = BASE_PAGE_LOCATORS()

    class IncorrectPage(Exception):
        pass

    def __init__(self, driver, config, logger):
        self.driver = driver
        self.url = config['web_url']
        self.logger = logger

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def web_wait(self):
        return WebDriverWait(self.driver, BASE_DELAY * N_RETRIES)

    @property
    def action_chains(self):
        return ActionChains(self.driver)

    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)

    def is_find(self, locator) -> bool:
        try:
            element = self.find(locator)
            if element:
                return True
            else:
                return False
        except selenium.common.exceptions.TimeoutException:
            return False

    @retry(N_RETRIES)
    def find(self, locator) -> WebElement:
        return self.web_wait.until(EC.presence_of_element_located(locator))

    @retry(N_RETRIES)
    def find_all(self, locator) -> list:
        return self.web_wait.until(EC.presence_of_all_elements_located(locator))

    @retry(N_RETRIES)
    def find_visible(self, locator) -> WebElement:
        return self.web_wait.until(EC.visibility_of_element_located(locator))

    def is_opened(self, timeout = BASE_DELAY * N_RETRIES, raise_error = True):
        def func():
            url_parsed = urlparse(self.url)
            url = url_parsed.netloc + url_parsed.path
            current_url_parsed = urlparse(self.driver.current_url)
            current_url = current_url_parsed.netloc + current_url_parsed.path
            return url == current_url
        try:
            return wait(func, timeout=timeout, check=True)
        except TimeoutError:
            if raise_error:
                raise BasePage.IncorrectPage(f"Page {self.driver.current_url} isn't {self.url}")
            return False

    def click(self, locator) -> WebElement:
        for i in range(N_RETRIES):
            try:
                button = self.web_wait.until(EC.element_to_be_clickable(locator))
                button.click()
                return button
            except selenium.common.exceptions.StaleElementReferenceException:
                if i >= N_RETRIES - 1:
                    raise
            except selenium.common.exceptions.ElementClickInterceptedException:
                if i >= N_RETRIES - 1:
                    raise

    def open(self):
        if not self.is_opened(raise_error=False):
            self.driver.get(self.url)
        return self.is_opened()
