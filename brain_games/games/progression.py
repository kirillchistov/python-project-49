# import prompt
from random import randint

GAME_DESCRIPTION = 'What number is missing in the progression?'


def brain_progression():
    random_num_1 = randint(1, 50)
    random_step = randint(1, 10)
    exp_len = randint(7, 10)
    random_num_last = random_num_1 + random_step * exp_len
    exp_progression = list(range(random_num_1, random_num_last, random_step))
    random_pos = randint(0, exp_len - 1)
    correct_answer = int(exp_progression[random_pos])
    exp_progression[random_pos] = '..'
    random_exp = " ".join(map(str, exp_progression))
    print(f'Question: {random_exp}')
    return correct_answer


def main():
    brain_progression()
