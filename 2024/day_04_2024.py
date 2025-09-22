#!/usr/bin/env python3
# day_04_2024.py - https://adventofcode.com/2024/day/4

import itertools


def neighbors_8(grid, pos):
    candidates = [
        pos + dx + dy for dx, dy in itertools.product([-1, 0, 1], [-1j, 0j, 1j])
    ]
    return [p for p in candidates if p != pos and p in grid]


def main():
    with open("day_04_2024.txt", "r") as fo:
        puzzle_input = fo.read()

    grid = {
        x + 1j * y: int(val)
        for y, line in enumerate(puzzle_input.split("\n"))
        for x, val in enumerate(line)
    }


if __name__ == "__main__":
    main()
