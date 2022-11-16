from urllib.parse import urljoin
from functools import reduce

questions = lambda base_url: urljoin(base_url, 'questions/')
question = lambda base_url, id: reduce(urljoin, [base_url, 'questions/', str(id)])
chain = lambda base_url: reduce(urljoin, [base_url, 'chain/'])
