#!/usr/bin/env python3
from brain_games import cli
# from brain_games import brain_even


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    cli.welcome_user()


if __name__ == '__main__':
    main()
