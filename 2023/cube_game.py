#!/usr/bin/env python3
# cube_game.py - a Python class representing a game for Advent of Code

import re


class CubeGame:
    def __init__(self, game, total_red=12, total_green=13, total_blue=14):
        # get the id number of the game, and split into rounds
        game_mo = re.search(r"Game\s(\d+):\s(.*)", game)
        game_id, game = game_mo.groups()

        self.id = int(game_id)
        game = [g.strip() for g in game.split(";")]

        rounds_possible = []
        cubes_needed = {
            "red": [],
            "green": [],
            "blue": [],
        }
        # get the round as some appreciable # of cubes
        for game_round in game:
            # init all values to avoid a ValueError
            red, green, blue = 0, 0, 0

            draws = [d.strip() for d in game_round.split(",")]
            for draw in draws:
                num, color = draw.split(" ")
                i = int(num)
                match color:
                    case "red":
                        red = i
                    case "green":
                        green = i
                    case "blue":
                        blue = i
                    case _:
                        # print an error message
                        print(f"Invalid color passed: {color}")
                        return

                cubes_needed[color].append(i)

            # evaluate the round for possibility
            # NOTE any one False will make the game impossible but for the sake
            # of following we will process all rounds anyway
            if all(
                [
                    red <= total_red,
                    green <= total_green,
                    blue <= total_blue,
                ]
            ):
                rounds_possible.append(True)
            else:
                rounds_possible.append(False)

        # determine if the game is possible
        if all(rounds_possible):
            self.is_possible = True
        else:
            self.is_possible = False

        # determine the game power
        self.power = 1
        for color, num_cubes in cubes_needed.items():
            self.power *= max(num_cubes)

        return
