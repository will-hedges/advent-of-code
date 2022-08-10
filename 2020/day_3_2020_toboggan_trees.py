#! python3
# day_3_2020.py

import logging
import os
from pathlib import Path


logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)


os.chdir(Path(__file__).parent)
with open('day_3_2020.txt', 'r') as infile:
    slope = [line.strip() for line in infile.readlines()]

moves = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def count_trees(terrain, shift):
    trees, x, y = 0, 0, 0
    slope_len = len(terrain)
    row_len = len(terrain[y])

    while y < slope_len:
        if x >= row_len:
            x = x % row_len

        loc = terrain[y][x]
        if loc == '#':
            trees += 1

        x += shift[0]
        y += shift[1]

    return trees


part_one = count_trees(slope, moves[1])
print(part_one)

part_two = 1
for move in moves:
    part_two *= count_trees(slope, move)
print(part_two)