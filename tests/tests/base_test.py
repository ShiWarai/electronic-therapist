from pytest import fixture
from _pytest.fixtures import FixtureRequest

from tests.ui import pages_fixtures

class BaseCase:

    @fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.main_page : pages_fixtures.MainPage = request.getfixturevalue("main_page")

