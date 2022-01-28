#!usr/bin/env python3

from random import randint
import prompt

user_name = ''


def welcome_user():
    print("Welcome to the Brain Games!")
    global user_name
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    return user_name


def greet_user():
    print(f'Congratulations, {user_name}!')


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        random_number = randint(1, 500)
        print(f'Question: {random_number}')

        if random_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        user_answer = prompt.string('You answer: ')

        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{right_answer}".')
            print(f'Let\'s try again, {user_name}!')
            break
    else:
        greet_user()
