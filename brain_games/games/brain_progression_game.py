from random import randint
from typing import Tuple

game_rules = "What number is missing in progression?"

# Number of progression elements
quantity = 10


def get_game_round() -> Tuple[str, str]:
    inc = randint(3, 15)
    hide_number = randint(1, quantity)
    right_answer = str(hide_number * inc)
    game_task = ""
    # Shifting the index by one
    for _ in range(1, quantity + 1):
        if _ != hide_number:
            d = str(inc * _)
            game_task += f" {d} "
        else:
            game_task += " .. "
    return game_task, right_answer
