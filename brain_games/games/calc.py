# import prompt
from random import randint
from random import choice

GAME_DESCRIPTION = 'What is the result of the expression?'


def brain_play():
    # global correct_answer
    operands = ['+', '-', '*']
    random_num_1 = randint(1, 100)
    random_oper = choice(operands)
    random_num_2 = randint(1, 100)
    question = f'{random_num_1} {random_oper} {random_num_2}'
    correct_answer = eval(question)
    # print(f'Question: {question}')
    return question, correct_answer


def main():
    brain_play()
