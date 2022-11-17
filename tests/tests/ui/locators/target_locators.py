from selenium.webdriver.common.by import By

class BASE_PAGE_LOCATORS:
    HTML_LOCATOR = (By.TAG_NAME, 'html')

class MAIN_PAGE_LOCATORS(BASE_PAGE_LOCATORS):
    PROFILE_MENU_BUTTON_LOCATOR = (By.CSS_SELECTOR, "div[class*='right-module-rightWrap']")
    LOGOUT_BUTTON_LOCATOR = (By.CSS_SELECTOR, "a[href='/logout']")
    TAB_LOCATOR = \
        lambda self, tab_name : (By.CSS_SELECTOR, f"a[href='/{tab_name}']" if tab_name != "help" else f"a[href*='/{tab_name}/']")