import pytest

from tests.api.base_api_case import BaseAPICase
from tests.ui.base_ui_case import BaseUICase


@pytest.mark.UI
class TestElectronicTherapistUI(BaseUICase):

    def test_enter(self):
        pass


@pytest.mark.API
class TestElectronicTherapistAPI(BaseAPICase):

    @pytest.mark.dependency(name='test_get_questions')
    def test_get_questions(self):
        questions = self.client.get_all_questions()

        assert questions is not None and questions != [] and questions != {}

    @pytest.mark.dependency(depends=["test_get_questions"])
    def test_get_question(self):
        questions = self.client.get_all_questions()
        id = questions[0]['id']  # Get first id

        question = self.client.get_question(id)
        assert question is not None and question != {}
        assert question['id'] == id
        assert question['text'] != '' and question['text'] is not None

    @pytest.mark.dependency(depends=["test_get_questions"])
    def test_negative_get_question(self):
        id = -1  # Ids > 0

        question = self.client.get_question(id)
        assert question is None or question == {}
