import logging
import os
import shutil

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

    return {'browser': browser, 'web_url': "http://localhost/", 'api_url': "http://localhost:8080/",
            'base_temp_dir': temp_dir}


@pytest.fixture(scope='function')
def driver(config, logger):
    browser = webdriver.Chrome(executable_path=config['browser'])
    browser.maximize_window()

    try:
        logger.info("Enter the website")
        browser.get(config['web_url'])

        yield browser
    except:
        logger.error("Couldn't enter the website")
    finally:
        browser.quit()


@pytest.fixture(scope='function')
def logger(temp_dir, config):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.DEBUG

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('selenium_test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


@pytest.fixture(scope='function')
def temp_dir(request, config):
    test_dir = os.path.join(config['base_temp_dir'],
                            request._pyfuncitem.nodeid.replace('/', '_').replace(':', '_'))
    os.makedirs(test_dir)
    return test_dir
