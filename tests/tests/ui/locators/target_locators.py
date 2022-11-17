from selenium.webdriver.common.by import By


class BASE_PAGE_LOCATORS:
    HTML_LOCATOR = (By.TAG_NAME, 'html')


class INDEX_PAGE_LOCATORS(BASE_PAGE_LOCATORS):
    START_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id*='start-btn']")

    TEXT_QUESTION_LOCATOR = (By.CSS_SELECTOR, "span[id*='question']")
    ANSWERS_BUTTONS_LOCATOR = (By.CSS_SELECTOR, "ul[id*='answers-group'] input[class*='answer']")
    ANSWER_BUTTON_LOCATOR = lambda answer: (By.CSS_SELECTOR, f"ul[id*='answers-group'] input[value*='{answer}']")
    ANSWER_TEXTAREA_LOCATOR = (By.CSS_SELECTOR, "textarea[id*='answer-text']")
    NEXT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "button[id*='next-question']")

    RESULT_TITLE_LOCATOR = (By.CSS_SELECTOR, "span[id*='result-title']")
    RESULT_TEXT_LOCATOR = (By.CSS_SELECTOR, "span[id*='result-text']")
    RESULT_RETURN_HOME_LOCATOR = (By.CSS_SELECTOR, "button[id*='return_home_button']")