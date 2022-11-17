from pytest import fixture

from tests.api.api_client import ApiClient


class BaseAPICase:

    @fixture(scope='function', autouse=True)
    def setup(self, config, logger):
        self.client = ApiClient(config['api_url'], logger)
        self.logger = logger

        self.logger.debug('Initial setup completed')
