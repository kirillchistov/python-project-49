import prompt

# Запрашиваем имя и выводим на экран приветствие
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')