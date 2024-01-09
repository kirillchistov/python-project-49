#!/usr/bin/env python3
from brain_games import cli

# выносим приветствие в отдельную функцию
def greet():
    print('Welcome to the Brain Games!')

# вызываем greet и welcome_user из cli
def main():
    greet()
    cli.welcome_user()    

# вызываем функции в main при импорте модуля
if __name__ == '__main__':
    main()