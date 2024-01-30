# import prompt
from random import randint
import math

GAME_DESC1 = 'Answer "yes" if given number is prime.'
GAME_DESC2 = 'Otherwise answer "no".'
DESCRIPTION = f'{GAME_DESC1} {GAME_DESC2}'


def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


def q_and_a():
    question = randint(1, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
