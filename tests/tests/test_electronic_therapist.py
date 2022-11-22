import time

import pytest

from tests.api.base_api_case import BaseAPICase
from tests.ui.base_ui_case import BaseUICase
from tests.utils.generators import generate_random_questions_and_answers_pairs,\
                                    generate_random_number_string, generate_answer


@pytest.mark.UI
class TestElectronicTherapistUI(BaseUICase):

    @pytest.mark.dependency(name='test_start_examination')
    def test_start_examination(self):
        self.index_page.start_new_examination()

        assert self.index_page.find_visible(self.index_page.locators.TEXT_QUESTION_LOCATOR)

    @pytest.mark.dependency(name="test_next_question", depends=["test_start_examination"])
    def test_next_question(self):
        self.index_page.start_new_examination()

        self.index_page.choose_any_answer(generate_random_number_string(10))

        last_new = self.index_page.next_question()

        assert last_new[0] != last_new[1]

    @pytest.mark.dependency(name="test_negative_next_question", depends=["test_start_examination"])
    def test_negative_next_question(self):
        self.index_page.start_new_examination()

        last_new = self.index_page.next_question()  # Without answer selection

        assert last_new[0] == last_new[1]

    @pytest.mark.dependency(name="test_get_result")
    def test_get_result(self):
        assert self.index_page.pass_examination(generate_answer)

        assert self.index_page.is_find(self.index_page.locators.RESULT_TEXT_LOCATOR)

    @pytest.mark.dependency(name="test_restart_examination", depends=["test_get_result"])
    def test_restart_examination(self):
        assert self.index_page.pass_examination(generate_answer)

        self.index_page.click(self.index_page.locators.RESULT_RETURN_HOME_LOCATOR)

        assert self.index_page.is_find(self.index_page.locators.START_BUTTON_LOCATOR)

    @pytest.mark.dependency(name="test_negative_restart_examination", depends=["test_get_result"])
    def test_negative_restart_examination(self):
        assert self.index_page.pass_examination(generate_answer)

        # self.index_page.click(self.index_page.locators.RESULT_RETURN_HOME_LOCATOR)

        assert not self.index_page.is_find(self.index_page.locators.START_BUTTON_LOCATOR)

@pytest.mark.API
class TestElectronicTherapistAPI(BaseAPICase):

    @pytest.mark.dependency(name='test_get_questions')
    def test_get_questions(self):
        questions = self.client.get_all_questions()

        assert questions is not None and questions != [] and questions != {}

    @pytest.mark.dependency(name="test_get_question", depends=["test_get_questions"])
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

    @pytest.mark.dependency(name="test_get_new_chain", depends=["test_get_question"])
    def test_get_new_chain(self):
        next_question_id = self.client.get_new_chain()

        assert next_question_id is not None
        assert self.client.get_question(next_question_id)['id'] == next_question_id

    @pytest.mark.dependency(name="test_get_next_chain", depends=["test_get_new_chain", "test_get_questions"])
    def test_get_next_chain(self):
        questions = self.client.get_all_questions()

        questions_and_answers = generate_random_questions_and_answers_pairs([questions[0], questions[-1]])

        next_question_id = self.client.get_next_chain(questions_and_answers)
        assert (next_question_id is None) or self.client.get_question(next_question_id)['id'] == next_question_id

    @pytest.mark.dependency(depends=["test_get_next_chain"])
    def test_get_result(self):
        questions = self.client.get_all_questions()

        questions_and_answers = generate_random_questions_and_answers_pairs([questions[0], questions[-1]])

        result: dict = self.client.get_result_by_answers(questions_and_answers)
        assert result is not None
        assert 'title' in result.keys() and 'text' in result.keys()
        assert result['title'] is not None and result['title'] != ""
        assert result['title'] in ("Следует обратиться к специалисту", "Есть причины беспокоится", "Всё хорошо")
        assert result['text'] is not None and result['text'] != ""

    @pytest.mark.dependency(depends=["test_get_next_chain"])
    def test_negative_get_result(self):
        questions_and_answers = None

        assert not self.client.get_result_by_answers(questions_and_answers)
