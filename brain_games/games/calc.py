# import prompt
from random import randint
from random import choice

DESCRIPTION = 'What is the result of the expression?'


def get_data():
    operands = ['+', '-', '*']
    random_num_1 = randint(1, 100)
    random_oper = choice(operands)
    random_num_2 = randint(1, 100)
    question = f'{random_num_1} {random_oper} {random_num_2}'

    if random_oper == '+':
        correct_answer = str(random_num_1 + random_num_2)
    elif random_oper == '-':
        correct_answer = str(random_num_1 - random_num_2)
    elif random_oper == '*':
        correct_answer = str(random_num_1 * random_num_2)

    return question, correct_answer
