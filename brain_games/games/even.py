# import prompt
from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_even():
    global correct_answer
    random_num = randint(0, 100)
    if random_num % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print(f'Question: {random_num}')
    return correct_answer


def main():
    brain_even()
