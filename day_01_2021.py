#!/usr/bin/env python

import os
from pathlib import Path


def sonar_sweep(lst):
    lst_copy = lst.copy()
    ans = 0
    v1 = lst_copy.pop(0)
    while lst_copy:
        v2 = lst_copy.pop(0)
        if v1 < v2:
            ans += 1
        v1 = v2
    return ans


def sliding_window(lst):
    windows = []
    while lst:
        window = [lst.pop(0)] + lst[:2]
        if len(window) == 3:
            windows.append(sum(window))
        else:
            break
    return sonar_sweep(windows)


def main():
    os.chdir(Path(__file__).parent)
    with open("day_01_input.txt", "r") as f:
        puzzle_input = [int(i) for i in f.readlines()]

    part_1 = sonar_sweep(puzzle_input)
    print(part_1)

    part_2 = sliding_window(puzzle_input)
    print(part_2)


if __name__ == "__main__":
    main()
