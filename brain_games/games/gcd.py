# import prompt
from random import randint
from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_data():
    random_num_1 = randint(1, 100)
    random_num_2 = randint(1, 100)
    question = f'{random_num_1} {random_num_2}'
    correct_answer = str(gcd(random_num_1, random_num_2))
    return question, correct_answer
