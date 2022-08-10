#!/usr/bin/env python3

import os
from pathlib import Path

import numpy as np

def part_one(heightmap):
    pass

def main():
    os.chdir(Path(__file__).parent)
    with open("test_input.txt", "r") as f:
    # with open("day_09_2021_input.txt", "r") as f:
        puzzle_input = [[int(n) for n in line.strip()] for line in f.readlines()]
    y = len(puzzle_input)
    x = len(puzzle_input[0])
    heightmap = []
    for row in puzzle_input:
        heightmap += row
    heightmap = np.array(heightmap).reshape(y, x)
    print(heightmap)
    """
        N
    W   X   E
        S
    """
    for row in heightmap:
        print(row)
        for h in row:
            print(h)




if __name__ == "__main__":
    main()
