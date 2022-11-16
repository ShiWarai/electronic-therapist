from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager, ChromeType

from tests.ui.pages_fixtures import *


@pytest.fixture()
def config():
    return {'web_url': "http://localhost/", 'api_url': "http://localhost:8080/"}


@pytest.fixture(scope='function')
def driver(config):
    options = Options()

    browser_name = config['browser']
    if browser_name == 'chrome':
        # There I haven't used a webdriver, because now it's working on Linux with Chromium correctly
        # options.add_argument("--remote-debugging-port=9222")  # Doesn't work without it on Ubuntu
        manager = ChromeDriverManager(version='latest', chrome_type=ChromeType.GOOGLE)
        browser = webdriver.Chrome(executable_path = manager.install(), options = options)
    else:
        raise RuntimeError(f'Unsupported browser: {browser_name}')

    browser.maximize_window()

    browser.get(config['default_url'])

    yield browser

    browser.quit()
