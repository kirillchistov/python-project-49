# import prompt
from random import randint
from random import choice

GAME_DESCRIPTION = 'What is the result of the expression?'


def brain_calc():
    global correct_answer
    operands = ['+', '-', '*']
    random_num_1 = randint(1, 100)
    random_oper = choice(operands)
    random_num_2 = randint(1, 100)
    random_exp = f'{random_num_1} {random_oper} {random_num_2}'
    correct_answer = eval(random_exp)
    print(f'Question: {random_exp}')
    return correct_answer


def main():
    brain_calc()
