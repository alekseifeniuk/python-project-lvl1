#!usr/bin/env python3

import prompt


def game_core(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.game_rules)
    for i in range(3):
        game_task, right_answer = game.rules()
        print(f'Question: {game_task}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == right_answer:
            print('Correct!')
        else:
            a = f'"{user_answer}" is wrong answer ;(. '
            b = f'Correct answer was "{right_answer}".'
            print(a + b)
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
