"""
Common logic for games: 1. Ask the user name and 2. print Welcome
3. Announce the rules and 4. Start the round
5. Ask the game question and 6. Prompt for answer
7. Evaluate answer against correct one and 8. Announce results
9. Iterate round or 10. exit game
"""
import prompt

GAMES_WELCOME = 'Welcome to the Brain Games!'
GAMES_ASKNAME = 'May I have your name? '
WRONG_ANSWER = 'is wrong answer;(. Correct answer was'


def play_game(game):
    print(GAMES_WELCOME)
    name = prompt.string(GAMES_ASKNAME)
    print(f'Hello, {name}!')
    description = game.GAME_DESCRIPTION
    print(description)

    rounds_won = 0  # start counting wins in a row
    while rounds_won < 3:
        game.main()
        ca = game.correct_answer  # get correct answer from game
        ug = input("Your answer: ")  # user guess
        if str(ug) == str(ca):
            print("Correct!")
            rounds_won += 1
        else:
            rounds_won = 0
            print(f"'{ug}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{ca}'.")
            print(f"Let's try again, {name}!")
            return

    if rounds_won == 3:
        print(f'Congratulations, {name}!')
        return
