"""
Common logic for games: 1. Ask the user name and 2. print Welcome
3. Announce the rules and 4. Start the round
5. Ask the game question and 6. Prompt for answer
7. Evaluate answer against correct one and 8. Announce results
9. Iterate round or 10. exit game
"""
import prompt

ROUNDS_TO_WIN = 3


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    for _ in range(ROUNDS_TO_WIN):
        #  game.main()
        question, correct_answer = game.generate_data()
        print(f'Question: {question}')
        user_guess = input("Your answer: ")
        if user_guess != correct_answer:
            print(f"'{user_guess}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
        print("Correct!")
    else:
        print(f'Congratulations, {name}!')
