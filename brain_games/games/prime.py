# import prompt
from random import randint
import math

GAME_DESC1 = 'Answer "yes" if given number is prime.'
GAME_DESC2 = 'Otherwise answer "no".'
GAME_DESCRIPTION = f'{GAME_DESC1} {GAME_DESC2}'


def is_prime(number):
    # return 'yes' if prime else return 'no'

    if number < 2:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


def brain_play():
    # global correct_answer
    question = randint(1, 100)
    # correct_answer = is_prime(question)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    # print(f'Question: {question}')
    return question, correct_answer


def main():
    brain_play()
