from selenium import webdriver

from tests.ui.pages_fixtures import *


def pytest_addoption(parser):
    parser.addoption('--browser', default=r'..\chromedriver.exe')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    return {'browser': browser, 'web_url': "http://localhost/", 'api_url': "http://localhost:8080/"}


@pytest.fixture(scope='function')
def driver(config):
    # change for another system
    browser = webdriver.Chrome(executable_path=config['browser'])
    browser.maximize_window()

    browser.get(config['web_url'])

    yield browser

    browser.quit()
