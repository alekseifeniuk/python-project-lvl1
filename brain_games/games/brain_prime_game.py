from random import randint
from typing import Tuple
from math import sqrt

game_rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_game_round() -> Tuple[str, str]:
    number = randint(2, 100)
    game_task = f"{number}"
    # Algorithm simple iteration of divisors
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            right_answer = "no"
            break
    else:
        right_answer = "yes"
    return game_task, right_answer
