from urllib.parse import urljoin

questions = lambda base_url: urljoin(base_url, 'questions')
question = lambda base_url, id: urljoin(base_url, 'questions', id)
chain = lambda base_url: urljoin(questions(base_url), 'chain')
