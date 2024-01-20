from brain_games.welcome import welcome_user
import prompt
from random import randint


def prime_check(number):
    # return 'yes' if prime else return 'no'
    correct_answer = 'yes'
    
    if number < 2:
        correct_answer = 'no'
    
    for i in range(2, number):
        if (number % i) == 0:               
            correct_answer = 'no'
    return correct_answer       


def randomize():
    random_number = randint(0, 100)
    return random_number


def brain_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    guess_in_row = 0

    while guess_in_row < 3:
        random_number = randomize()
        print('Question:', {random_number})
        user_answer = prompt.string('Your answer: ')
        ua = user_answer
        correct_answer = prime_check(random_number)
        ca = correct_answer
        if user_answer == correct_answer:
            print('Correct!')
            guess_in_row += 1
        else:
            print(f'{ua} is wrong answer;(. Correct answer was {ca}.')
            print(f"Let's try again, {name}!")
            guess_in_row = 0
            return None

    if guess_in_row == 3:
        print(f'Congratulations, {name}!')
        return None
