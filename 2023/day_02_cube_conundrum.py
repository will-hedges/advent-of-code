#!/usr/bin/env python3
# day_02_cube_conundrum.py - https://adventofcode.com/2023/day/2

from cube_game import CubeGame


def main():
    with open("input.txt") as fo:
        games = fo.readlines()

    possible_game_ids = []
    game_powers = []

    for game in games:
        cg = CubeGame(game)
        if cg.is_possible:
            possible_game_ids.append(cg.id)
        game_powers.append(cg.power)

    # part one
    print(sum(possible_game_ids))
    # part two
    print(sum(game_powers))

    return


if __name__ == "__main__":
    main()
