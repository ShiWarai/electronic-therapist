import json

import requests

from tests.api import api_urls
from tests.api.api_exceptions import *


class ApiClient:

    def __init__(self, base_url, logger):
        self.base_url = base_url
        self.logger = logger

        self.session = requests.Session()

    def __request(self, request_type: str, url: str, headers=None, data: dict = {}, expected_error=None,
                  json_expected=False):

        self.logger.info(f"Request to {url}, type {request_type}")
        self.logger.debug(f"Data = {data}")
        response = self.session.request(request_type, url, headers=headers, data=data)

        self.logger.info(f"Response status code - {response.status_code}")
        self.logger.info(f"Response content: {response.content}")

        if json_expected:
            if (expected_error and response.status_code == expected_error) or not expected_error:
                return json.loads(response.content.decode('utf-8'))
            else:
                raise UnexpectedResponse(f"Response {response} isn't expected")
        else:
            return response

    def get_all_questions(self):
        url = api_urls.questions(self.base_url)
        json_data = self.__request('GET', url, expected_error=200, json_expected=True)
        return json_data

    def get_question(self, id):
        url = api_urls.question(self.base_url, id)
        try:
            json_data = self.__request('GET', url, expected_error=200, json_expected=True)
            return json_data
        except UnexpectedResponse:
            return None

    def get_new_chain(self):
        url = api_urls.chain(self.base_url)
        json_data = self.__request('GET', url, expected_error=200, json_expected=True)
        return json_data

    def get_next_chain(self, questions_and_answers: list):
        url = api_urls.chain(self.base_url)
        json_data = self.__request('PUT', url, data=json.dumps(questions_and_answers),
                                   expected_error=200, json_expected=True)
        return json_data

    def get_result_by_answers(self, questions_and_answers: list):
        url = api_urls.answers(self.base_url)
        json_data = self.__request('POST', url, data=json.dumps(questions_and_answers),
                                   expected_error=200, json_expected=True)

        return json_data