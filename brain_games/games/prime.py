# import prompt
from random import randint
import math

DESCRIPTION = '''Answer "yes" if given number is prime.
Otherwise answer "no".'''


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


def get_data():
    question = randint(1, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
