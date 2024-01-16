#!/usr/bin/env python3
import prompt
from random import randint
from random import choice


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def randomize():
    expr_list = ['+', '-', '*']
    rnd_num_1 = randint(1, 99)
    rnd_oper = choice(expr_list)
    rnd_num_2 = randint(1, 99)
    rnd_exp = f'{rnd_num_1} {rnd_oper} {rnd_num_2}'
    return (rnd_num_1, rnd_oper, rnd_num_2, rnd_exp)


def expression_calc(num_1, operand, num_2):
    if operand == '+':
        return num_1 + num_2
    elif operand == '-':
        return num_1 - num_2
    elif operand == '*':
        return num_1 * num_2
    else:
        print('Unknown operand, please restart')
        return None


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    guess_in_row = 0
    while guess_in_row < 3:
        # rnd_num_1 = randomize().rnd_num_1
        # rnd_oper = randomize().rnd_oper
        # rnd_num_2 = randomize().rnd_num_2
        
        random_exp = randomize.rnd_exp
        random_exp_result = eval(random_exp)
        print(random_exp_result, 'vs', random_exp)
        print(f'Question: {random_exp}')
        user_guess = prompt.string('Your answer: ')
        if (user_guess == random_exp_result):
            print('Correct!')
            guess_in_row += 1
        else:
            print(f'{user_guess} is wrong answer;(.')
            print(f'Correct answer was {random_exp_result}')
            print(f"Let's try again, {name}!")
            guess_in_row = 0
    if guess_in_row == 3:
        print(f'Congratulations, {name}!')
        return None


def main():
    brain_calc()


if __name__ == '__main__':
    main()
