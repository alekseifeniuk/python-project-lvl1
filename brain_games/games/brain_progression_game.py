from random import randint
from typing import Tuple

game_rules = "What number is missing in progression?"
MIN_SIZE = 5
MAX_SIZE = 10
MAX_STEP = 10
MAX_START = 10


def get_game_round() -> Tuple[str, str]:
    begin = randint(0, MAX_START)
    end = randint(MIN_SIZE, MAX_SIZE)
    inc = randint(2, MAX_STEP)
    sequence = list(range(begin, begin + end * inc, inc))
    index = randint(0, len(sequence) - 1)
    right_answer = str(sequence[index])
    sequence[index] = ".."
    game_task = " ".join(str(i) for i in sequence)
    return game_task, right_answer
