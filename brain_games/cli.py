#!usr/bin/env python3

import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def print_rules(game):
    print(game.game_rules)


def question(game_task):
    print(f'Question: {game_task}')


def answer():
    u_answer = prompt.string('Your answer: ')
    return u_answer


def correct_answer():
    print('Correct!')


def congratulate_user(user_name):
    print(f'Congratulations, {user_name}!')


def game_over(user_answer, right_answer, user_name):
    print(f'"{user_answer}" is wrong answer ;(. '
          f'Correct answer was "{right_answer}".\n'
          f"Let's try again, {user_name}!")
