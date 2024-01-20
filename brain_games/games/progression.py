import prompt
from random import randint
from brain_games.welcome import welcome_user
#  DOD: guess the number missing in given progression


def brain_progression():
    name = welcome_user()
    print('What number is missing in the progression?')
    guess_in_row = 0

    while guess_in_row < 3:
        rnd_num_1 = randint(1, 50)
        rnd_step = randint(1, 10)
        exp_len = randint(7, 10)
        rnd_num_last = rnd_num_1 + rnd_step * exp_len

        exp_progression = list(range(rnd_num_1, rnd_num_last, rnd_step))
        rnd_pos = randint(0, exp_len - 1)

        rnd_exp_result = int(exp_progression[rnd_pos])
        exp_progression[rnd_pos] = '..'
        rnd_exp = " ".join(map(str, exp_progression))
        rer = rnd_exp_result

        print(f'Question: {rnd_exp}')
        user_guess = int(prompt.string('Your answer: '))
        ug = user_guess

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
