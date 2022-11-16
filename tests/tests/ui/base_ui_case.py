from _pytest.fixtures import FixtureRequest
from pytest import fixture

from tests.ui import pages_fixtures


class BaseUICase:

    @fixture(scope='function', autouse=True)
    def setup(self, driver, config, logger, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.logger = logger

        self.logger.debug('Initial setup completed')

        self.index_page: pages_fixtures.IndexPage = request.getfixturevalue("index_page")
