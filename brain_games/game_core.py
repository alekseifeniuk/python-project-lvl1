#!usr/bin/env python3

from brain_games.cli import welcome_user, print_rules
from brain_games.cli import question, answer, correct_answer
from brain_games.cli import game_over, congratulate_user
from brain_games.games import brain_even_rules


def game_core(game):
    user_name = welcome_user()
    print_rules(brain_even_rules)
    for i in range(3):
        game_task, right_answer = game.rules()
        question(game_task)
        user_answer = answer()

        if user_answer == right_answer:
            correct_answer()
        else:
            game_over(user_answer, right_answer, user_name)
            break
    else:
        congratulate_user(user_name)
