#!/usr/bin/env python3
import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def even_check(number):
    # return 'yes' if number % 2 == 0 else: return 'no'
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def randomize():
    random_number = randint(0, 99)
    return random_number


def brain_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    guess_in_row = 0
    while guess_in_row < 3:
        random_number = randomize()
        print('Question:', {random_number})
        user_guess = prompt.string('Your answer: ')
        if (random_number % 2 == 0):
            if user_guess == 'yes':
                print('Correct!')
                guess_in_row += 1
            else:
                print('"yes" is wrong answer;(.')
                print('Correct answer was "no".')
                print(f"Let's try again, {name}!")
                guess_in_row = 0
        elif (random_number % 2 != 0):
            if user_guess == 'no':
                print('Correct!')
                guess_in_row += 1
            else:
                print('"no" is wrong answer;(.')
                print('Correct answer was "yes".')
                print(f"Let's try again, {name}!")
                guess_in_row = 0
    if guess_in_row == 3:
        print(f'Congratulations, {name}!')
        return None


def main():
    brain_even()


if __name__ == '__main__':
    main()
