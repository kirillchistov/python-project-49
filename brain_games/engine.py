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
    description = game.GAME_DESCRIPTION
    # question = game.GAME_QUESTION
    print(description)

    # rounds_won = 0  # start counting wins in a row
    for r in range(ROUNDS_TO_WIN):
        game.main()
        question, correct_answer = game.brain_play()
        ca = correct_answer  # get correct answer from game
        print(f'Question: {question}')
        ug = input("Your answer: ")  # user guess
        if str(ug) != str(ca):
            print(f"'{ug}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{ca}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    else:
        print(f'Congratulations, {name}!')
        return
