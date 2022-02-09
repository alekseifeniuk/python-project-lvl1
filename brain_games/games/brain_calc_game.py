from random import randint, choice
from typing import Tuple

game_rules = "What is the result of the expression?"


def multiplication(one: int, two: int) -> Tuple[str, str]:
    game_task = f"{one} * {two}"
    right_answer = str(one * two)
    return game_task, right_answer


def addition(one: int, two: int) -> Tuple[str, str]:
    game_task = f"{one} + {two}"
    right_answer = str(one + two)
    return game_task, right_answer


def subtraction(one: int, two: int) -> Tuple[str, str]:
    game_task = f"{one} - {two}"
    right_answer = str(one - two)
    return game_task, right_answer


def get_game_round() -> Tuple[str, str]:
    number_one = randint(1, 20)
    number_two = randint(1, 20)
    operations = [
        multiplication(number_one, number_two),
        addition(number_one, number_two),
        subtraction(number_one, number_two),
    ]
    game_task, right_answer = choice(operations)
    return game_task, right_answer
