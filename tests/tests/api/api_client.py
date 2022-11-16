import json

import requests

from tests.api import api_urls
from tests.api.api_exceptions import *


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url

        self.session = requests.Session()

    def __request(self, request_type: str, url: str, headers=None, data: dict = {}, expected_error=None,
                  json_expected=False):

        # self.logger.info(f"Request to {url}, type {request_type}")
        # self.logger.debug(f"Data = {data}")
        response = self.session.request(request_type, url, headers=headers, data=data)

        # self.logger.info(f"Response status code - {response.status_code}")
        # self.logger.info(f"Response content: {response.content}")

        if json_expected:
            if (expected_error and response.status_code == expected_error) or not expected_error:
                return json.loads(response.content.decode('utf-8'))
            else:
                raise UnexpectedResponse(f"Response {response} isn't expected")
        else:
            return response

    def get_all_questions(self):
        url = api_urls.questions(self.base_url)
        try:
            json_data = self.__request('GET', url, expected_error=200, json_expected=True)
            return json_data
        except UnexpectedResponse:
            return None
