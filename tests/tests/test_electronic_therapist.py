import pytest

from tests.api.base_api_case import BaseAPICase
from tests.ui.base_ui_case import BaseUICase


@pytest.mark.UI
class TestElectronicTherapistUI(BaseUICase):

    def test_enter(self):
        pass


@pytest.mark.API
class TestElectronicTherapistAPI(BaseAPICase):

    def test_questions(self):
        questions = self.client.get_all_questions()

        assert questions is not None
        assert questions != []
        assert questions != {}
