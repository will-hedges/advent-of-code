import os
from pathlib import Path


def letter_to_value(move):
    match move:
        case "A" | "X":
            return 1
        case "B" | "Y":
            return 2
        case "C" | "Z":
            return 3


def main():
    os.chdir(Path(__file__).parent)
    with open("day_02_2022.txt", "r") as infile:
        guide = [
            tuple(map(letter_to_value, pair.strip().split(" ")))
            for pair in infile.readlines()
        ]

    ### PART ONE ###
    poss = set(guide)
    outcomes = {}
    for p in poss:
        outcomes[p] = guide.count(p)

    score = 0
    for o in outcomes:
        opp, me = o
        match (opp, me):
            # wins
            case (3, 1) | (1, 2) | (2, 3):
                score += 6 * outcomes[o]
                score += me * outcomes[o]
            # losses
            case (1, 3) | (2, 1) | (3, 2):
                score += me * outcomes[o]
            # ties
            case _:
                score += 3 * outcomes[o]
                score += me * outcomes[o]
    print(score)  # 14375


if __name__ == "__main__":
    main()
