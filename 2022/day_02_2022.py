import os
from pathlib import Path


def get_point_value(move):
    match move:
        case "rock":
            return 1
        case "paper":
            return 2
        case "scissors": 
            return 3


def letter_to_rps(move):
    match move:
        case "A" | "X":
            return "rock"
        case "B" | "Y":
            return "paper"
        case "C" | "Z":
            return "scissors"


def score_game(game):
    their_move, my_move = game
    
    match (game):
        # wins
        case ("rock", "paper") | ("paper", "scissors") | ("scissors", "rock"):
            return 6 + get_point_value(my_move)
        # losses
        case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            return 0 + get_point_value(my_move)
        # draws
        case _:
            return 3 + get_point_value(my_move)


def part_one():
    with open("day_02_2022.txt", "r") as infile:
        guide = [
            tuple(map(letter_to_rps, pair.strip().split(" ")))
            for pair in infile.readlines()
        ]
    
    outcomes = set(guide)
    game_breakdowns = {}
    for outcome in outcomes:
        game_breakdowns[outcome] = guide.count(outcome)

    score = 0
    for outcome, num_of_games in game_breakdowns.items():
        their_move, my_move = outcome
        score += score_game(outcome) * num_of_games 

    return score  


def main():
    os.chdir(Path(__file__).parent)

    print(part_one()) # 14375


if __name__ == "__main__":
    main()
