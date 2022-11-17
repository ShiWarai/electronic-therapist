from selenium.webdriver.common.by import By


class BASE_PAGE_LOCATORS:
    HTML_LOCATOR = (By.TAG_NAME, 'html')


class INDEX_PAGE_LOCATORS(BASE_PAGE_LOCATORS):
    START_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id*='start-btn']")
    TEXT_QUESTION_LOCATOR = (By.CSS_SELECTOR, "span[id*='question']")
    NEXT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id*='next-question']")

    RESULT_TITLE_LOCATOR = (By.CSS_SELECTOR, "span[id*='result-title']")
    RESULT_TEXT_LOCATOR = (By.CSS_SELECTOR, "span[id*='result-text']")