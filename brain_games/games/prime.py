# import prompt
from random import randint

GAME_DESC1 = 'Answer "yes" if given number is prime.'
GAME_DESC2 = 'Otherwise answer "no".'
GAME_DESCRIPTION = f'{GAME_DESC1} {GAME_DESC2}'


def prime_check(number):
    # return 'yes' if prime else return 'no'
    correct_answer = 'yes'

    if number < 2:
        correct_answer = 'no'

    for i in range(2, number):
        if (number % i) == 0:
            correct_answer = 'no'
    return correct_answer


def brain_prime():
    global correct_answer
    random_num = randint(1, 100)
    correct_answer = prime_check(random_num)
    print(f'Question: {random_num}')
    return correct_answer


def main():
    brain_prime()
