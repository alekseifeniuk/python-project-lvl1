from random import randint
from typing import Tuple

game_rules = "Find the greatest common divisor of given numbers."


def get_game_round() -> Tuple[str, str]:
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    game_task = f"{number_one} {number_two}"
    # Euclid's GCD algorithm
    while number_one != 0 and number_two != 0:
        if number_one > number_two:
            number_one = number_one % number_two
        else:
            number_two = number_two % number_one
    right_answer = str(number_one + number_two)
    return game_task, right_answer
