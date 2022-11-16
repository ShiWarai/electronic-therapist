from selenium import webdriver
from tests.ui.pages_fixtures import *

@pytest.fixture()
def config():
    url = "http://localhost:8080/"

    return {'url': url}

@pytest.fixture(scope='function')
def driver(config):
    # change for another system
    browser = webdriver.Chrome(executable_path=r'D:\YandexDisk\Study\Тестирование и варификация ПО\Практическая работа 3\electronic-therapist\tests\chromedriver.exe')
    browser.maximize_window()

    browser.get(config['url'])

    yield browser

    browser.quit()