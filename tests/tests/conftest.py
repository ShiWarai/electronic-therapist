from selenium import webdriver
from tests.ui.pages_fixtures import *

def pytest_addoption(parser):
    parser.addoption('--browser', default=r'..\chromedriver.exe')
    parser.addoption('--temp', default=r'..\temp')


@pytest.fixture(scope='session')
def config(request):
    browser = request.config.getoption('--browser')
    temp_dir = request.config.getoption('--temp')

    if not hasattr(config, 'workerinput'):  # in master only
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

    return {'browser': browser, 'web_url': "http://localhost/", 'api_url': "http://localhost:8000/",
            'base_temp_dir': temp_dir}


@pytest.fixture(scope='function')
def driver(config):
    # change for another system
    browser = webdriver.Chrome(executable_path=r'D:\YandexDisk\Study\Тестирование и варификация ПО\Практическая работа 3\electronic-therapist\tests\chromedriver.exe')
    browser.maximize_window()

    browser.get(config['url'])

    yield browser

    browser.quit()