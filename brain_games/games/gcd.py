import prompt
from random import randint
from math import gcd
#  from brain_games.cli import welcome_user
#  DOD: calculate GCD of two random numbers
#  What it does: cycle division of a and b until we get b = zero.
#  Inside the cycle we swap a and b so a becomes the remainder of the division
#  

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

#  def find_gcd(rnd_num_1, rnd_num_2):
#    if rnd_num_2 == 0:
#        return rnd_num_1
#    else:
#        while rnd_num_2:
#            rnd_num_1, rnd_num_2 = rnd_num_2, rnd_num_1 % rnd_num_2
#            return rnd_num_1


def brain_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers')
    guess_in_row = 0

    while guess_in_row < 3:
        rnd_num_1 = randint(1, 100)
        rnd_num_2 = randint(1, 100)
        rnd_exp = f'{rnd_num_1} {rnd_num_2}'
        rnd_exp_result = gcd(rnd_num_1, rnd_num_2)
        rer = rnd_exp_result

        print(f'Question: {rnd_exp}')
        user_guess = int(prompt.string('Your answer: '))
        ug = user_guess
        # print(f'{rer} vs {ug}')

        if (user_guess == rnd_exp_result):
            print('Correct!')
            guess_in_row += 1
        else:
            print(f'{ug} is wrong answer;(. Correct answer was {rer}.')
            print(f"Let's try again, {name}!")
            return None

    if guess_in_row == 3:
        print(f'Congratulations, {name}!')
        return None
