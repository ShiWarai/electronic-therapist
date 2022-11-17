import random
import string
from datetime import datetime

random.seed(datetime.now()) # Set pseudo random seed

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

def generate_random_number_string(length):
    letters = string.digits
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string