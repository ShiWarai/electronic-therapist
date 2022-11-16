import pytest
from urllib.parse import urljoin

from tests.base_test import BaseCase
from tests.utils.generators import generate_random_string, generate_random_number_string

@pytest.mark.UI
class TestElectronicTherapistUI(BaseCase):

    def test_enter(self):
        pass

@pytest.mark.API
class TestElectronicTherapistAPI:

    def test_questions(self):
        pass