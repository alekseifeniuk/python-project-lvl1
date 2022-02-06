#!usr/bin/env python3

from brain_games.cli import (
    welcome_and_acknowledge_user,
    print_rules,
    ask_question,
    ask_answer,
    correct_answer,
    congratulate_user,
    game_over)


def game_core(game):
    user_name = welcome_and_acknowledge_user()
    print_rules(game.game_rules)
    for _ in range(3):
        game_task, right_answer = game.get_game_round()
        ask_question(game_task)
        user_answer = ask_answer()

        if user_answer == right_answer:
            correct_answer()
        else:
            game_over(user_answer, right_answer, user_name)
            break
    else:
        congratulate_user(user_name)
