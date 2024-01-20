from brain_games.welcome import welcome_user
import prompt
from random import randint
from random import choice


def brain_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    guess_in_row = 0
    expr_list = ['+', '-', '*']

    while guess_in_row < 3:
        rnd_num_1 = randint(1, 100)
        rnd_oper = choice(expr_list)
        rnd_num_2 = randint(1, 100)
        rnd_exp = f'{rnd_num_1} {rnd_oper} {rnd_num_2}'
        rnd_exp_result = eval(rnd_exp)
        rer = rnd_exp_result

        print(f'Question: {rnd_exp}')
        user_guess = int(prompt.string('Your answer: '))
        ug = user_guess
        # print(f'{rnd_exp_result} vs {user_guess}')

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
