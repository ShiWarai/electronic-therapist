import random
import string
from datetime import datetime

random.seed(datetime.now())  # Set pseudo random seed


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_number_string(length):
    letters = string.digits
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_questions_and_answers_pairs(questions):
    questions_and_answers = list()

    for question in questions:
        answer = generate_random_string(8) if len(question['answers']) == 0 else question['answers'][0]
        questions_and_answers.append({"question_id": question['id'], 'answer': answer})

    return questions_and_answers


def generate_answer(question: str) -> str:
    if question.find('?'):
        return 'Не уверен'
    else:
        return generate_random_string(24)
