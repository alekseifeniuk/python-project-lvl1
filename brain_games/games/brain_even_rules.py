#!usr/bin/env python3

from random import randint

game_rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def rules():
    game_task = randint(1, 500)
    if game_task % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_task, right_answer
