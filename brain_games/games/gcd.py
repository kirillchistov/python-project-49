# import prompt
from random import randint
from math import gcd

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def brain_play():
    # global correct_answer
    random_num_1 = randint(1, 100)
    random_num_2 = randint(1, 100)
    question = f'{random_num_1} {random_num_2}'
    correct_answer = str(gcd(random_num_1, random_num_2))
    # print(f'Question: {question}')
    return question, correct_answer


def main():
    brain_play()
