#!/usr/bin/env python3
import prompt
from random import randint
from random import choice


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


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
    expr_list = ['+', '-', '*']

    while guess_in_row < 3:
        rnd_num_1 = randint(1, 99)
        rnd_oper = choice(expr_list)
        rnd_num_2 = randint(1, 99)
        rnd_exp = f'{rnd_num_1} {rnd_oper} {rnd_num_2}'
        rnd_exp_result = eval(rnd_exp)
        
        print(f'Question: {rnd_exp}')
        user_guess = int(prompt.string('Your answer: '))
        # print(f'{rnd_exp_result} vs {user_guess}')
        
        if (user_guess == rnd_exp_result):
            print('Correct!')
            guess_in_row += 1
        else:
            print(f'{user_guess} is wrong answer;(. Correct answer was {rnd_exp_result}.')
            print(f"Let's try again, {name}!")
            return None
        
    if guess_in_row == 3:
        print(f'Congratulations, {name}!')
        return None


def main():
    brain_calc()


if __name__ == '__main__':
    main()
