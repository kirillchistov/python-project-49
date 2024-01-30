# import prompt
from random import randint

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0

def brain_play():
    # global correct_answer
    question = randint(0, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    # print(f'Question: {question}')
    return question, correct_answer


def main():
    brain_play()
