import selenium.common.exceptions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC

from tests.ui.locators.target_locators import BASE_PAGE_LOCATORS

CLICK_RETRY = 3
TIME_DELAY = 3

def retry(func):
    def wrapper(*args, **kwargs):
        for i in range(CLICK_RETRY):
            try:
                return func(*args, **kwargs)
            except selenium.common.exceptions.TimeoutException:
                if i >= CLICK_RETRY - 1:
                    raise
    return wrapper

class BasePage:

    locators = BASE_PAGE_LOCATORS()

    # setting driver for all tests of this class
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, TIME_DELAY)

    @retry
    def find(self, locator) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))


    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                button = self.wait.until(EC.element_to_be_clickable(locator))
                button.click()
                return button
            except selenium.common.exceptions.StaleElementReferenceException:
                if i >= CLICK_RETRY - 1:
                    raise
            except selenium.common.exceptions.ElementClickInterceptedException:
                if i >= CLICK_RETRY - 1:
                    raise

    def get_auth_username(self) -> str:
        return self.find(self.locators.HTML_LOCATOR).get_attribute('data-ga-auth-username')