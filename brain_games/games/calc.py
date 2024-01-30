# import prompt
from random import randint
from random import choice

DESCRIPTION = 'What is the result of the expression?'


def q_and_a():
    operands = ['+', '-', '*']
    random_num_1 = randint(1, 100)
    random_oper = choice(operands)
    random_num_2 = randint(1, 100)
    question = f'{random_num_1} {random_oper} {random_num_2}'
    correct_answer = eval(question)
    return question, correct_answer
