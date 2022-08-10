#!/usr/bin/env python

from collections import Counter
import os
from pathlib import Path


def find_points_on_line(list_of_2_points):
    list_of_2_points = sorted(list_of_2_points)
    x1, y1 = list_of_2_points[0]
    x2, y2 = list_of_2_points[1]

    if x1 == x2:
        a, b = sorted([y2, y1])
        points = [(x1, y) for y in range(a, b + 1)]
    elif y1 == y2:
        a, b = sorted([x1, x2])
        points = [(x, y1) for x in range(a, b + 1)]
    else:
        slope = int((y2 - y1) / (x2 - x1))
        xs = [x for x in range(x1, x2 + 1)]
        ys = [y for y in range(y1, y2 + slope, slope)]
        points = list(zip(xs, ys))

    return sorted(points)


def main():
    os.chdir(Path(__file__).parent)
    # with open("test_input.txt", "r") as f:
    with open("day_05_2021_input.txt", "r") as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    lines = [
        [tuple(int(n) for n in point.split(",")) for point in line.split(" -> ")]
        for line in puzzle_input
    ]

    all_points = []
    for line in lines:
        points = find_points_on_line(line)
        if points is not None:
            all_points += points

    part_one = len([k for k, v in Counter(all_points).items() if v >= 2])
    print(part_one)


if __name__ == "__main__":
    main()
