#!usr/bin/env python3

from random import randint, choice

game_rules = "What is the result of the expression?"


def multiplication(one, two):
    game_task = f"{one} * {two}"
    right_answer = str(one * two)
    return game_task, right_answer


def addition(one, two):
    game_task = f"{one} + {two}"
    right_answer = str(one + two)
    return game_task, right_answer


def subtraction(one, two):
    game_task = f"{one} - {two}"
    right_answer = str(one - two)
    return game_task, right_answer


def get_game_round():
    number_one = randint(1, 20)
    number_two = randint(1, 20)
    list_operations = [
        multiplication(number_one, number_two),
        addition(number_one, number_two),
        subtraction(number_one, number_two),
    ]
    game_task, right_answer = choice(list_operations)
    return game_task, right_answer
