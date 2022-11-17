from typing import List

from fastapi import FastAPI, Response
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

questions = (
    {'id': 1, 'text': 'У вас есть проблемы со сном?', 'answers': ['Да', 'Нет', 'Не уверен']},
    {'id': 2, 'text': 'Опишите проблему со сном', 'answers': []},
    {'id': 3, 'text': 'У вас есть проблема с памятью?', 'answers': ['Да', 'Нет', 'Не уверен']},
    {'id': 4, 'text': 'Опишите проблему с памятью', 'answers': []}
)

paths = {
    1: {
        0: 2,
        1: None,
        2: 3
    },
    2: None,
    3: {
        0: 4,
        1: 2,
        2: None
    },
    4: None
}

chain_counter = 0
chains = list()


class Result:
    def __init__(self, title, text):
        self.title = title
        self.text = text


class AnswerBody(BaseModel):
    question_id: int
    answer: str


class Chain:

    # @staticmethod
    # def get_next(questions_and_answers: list) -> int:
    #     if questions_and_answers:
    #         question = questions_and_answers[len(questions_and_answers) - 1][0]
    #
    #         next_id = questions.index(question) + 1
    #
    #         if next_id < len(questions):
    #             return questions[next_id]['id']
    #         else:
    #             return None
    #
    #     return questions[0]['id']

    @staticmethod
    def get_next(questions_and_answers: list) -> int:
        if questions_and_answers:
            question = questions_and_answers[len(questions_and_answers) - 1][0]
            answer = questions_and_answers[len(questions_and_answers) - 1][1]

            if len(question['answers']) > 0:
                path = paths.get(question['id'])[question['answers'].index(answer)]
            else:
                path = paths.get(question['id'])

            return path

        return questions[0]['id']

    @staticmethod
    def resolve_chain(questions_and_answers: list) -> Result:
        title = "Пока тест"
        text = "Пока тут ничего нет, но скоро будет..."
        return Result(title, text)


@app.get("/questions")
async def get_all_questions():
    return questions


@app.get("/questions/{id}")
async def get_question_by_id(id: int, response: Response):
    question = None
    response.status_code = 404

    for q in questions:
        if q['id'] == id:
            question = q
            response.status_code = 200
            break

    return question


@app.get("/chain")
async def get_new_questions_chain():
    return Chain.get_next(None)


def expose_que_and_ans(answer_bodies: List[AnswerBody]):
    questions_and_answers = list()

    for answer_body in answer_bodies:
        question = None
        if not (answer_body.answer is not None and answer_body.answer != ""):
            return None

        for q in questions:
            if q['id'] == answer_body.question_id:
                question = q
                break

        if question is not None:
            questions_and_answers.append((question, answer_body.answer))
        else:
            return None

    return questions_and_answers


@app.put("/chain")
async def get_next_chain_question(answer_bodies: List[AnswerBody], response: Response):
    questions_and_answers = expose_que_and_ans(answer_bodies)

    if questions_and_answers is not None:
        return Chain.get_next(questions_and_answers)
    else:
        response.status_code = 424
        return None
