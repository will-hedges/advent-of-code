import os
from pathlib import Path


def letter_to_rps(move):
    match move:
        case "A" | "X":
            return "rock"
        case "B" | "Y":
            return "paper"
        case "C" | "Z":
            return "scissors"


def letter_to_move_or_outcome(letter):
    match letter:
        case "A" | "B" | "C":
            return letter_to_rps(letter)
        case "X":
            return "loss"
        case "Y":
            return "draw"
        case "Z":
            return "win"


def get_corresponding_move(move, outcome):
    if outcome == "draw":
        return move

    match move:
        case "rock":
            if outcome == "loss":
                return "scissors"
            return "paper"
        case "paper":
            if outcome == "loss":
                return "rock"
            return "scissors"
        case "scissors":
            if outcome == "loss":
                return "paper"
            return "rock"


def read_in_and_translate_guide(converter_fxn):
    with open("day_02_2022.txt", "r") as infile:
        guide = [
            tuple(map(converter_fxn, pair.strip().split(" ")))
            for pair in infile.readlines()
        ]

    outcomes = set(guide)
    game_breakdowns = {}
    for outcome in outcomes:
        game_breakdowns[outcome] = guide.count(outcome)

    return game_breakdowns


def score_game(game):
    moves = ("rock", "paper", "scissors")

    my_move = game[1]

    match (game):
        # wins
        case ("rock", "paper") | ("paper", "scissors") | ("scissors", "rock"):
            return 6 + moves.index(my_move) + 1
        # losses
        case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            return 0 + moves.index(my_move) + 1
        # draws
        case _:
            return 3 + moves.index(my_move) + 1


def part_one():
    games = read_in_and_translate_guide(letter_to_rps)

    score = 0
    for outcome, num_of_games in games.items():
        score += score_game(outcome) * num_of_games

    return score


def part_two():
    games = read_in_and_translate_guide(letter_to_move_or_outcome)

    score = 0
    for game, num_of_games in games.items():
        opp, outcome = game
        my_move = get_corresponding_move(opp, outcome)
        game = (opp, my_move)
        score += score_game(game) * num_of_games

    return score


def main():
    os.chdir(Path(__file__).parent)
    print(part_one())  # 14375
    print(part_two())  # 10274


if __name__ == "__main__":
    main()
