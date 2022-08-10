# day_02_2015.py - https://adventofcode.com/2015/day/2


import os
from pathlib import Path


def paper_and_ribbon(dim):
    l, w, h = sorted([int(i) for i in dim.split("x")])
    a, b, c = [(l * w), (w * h), (h * l)]

    surface_area = (2 * a) + (2 * b) + (2 * c)
    paper = surface_area + min(a, b, c)

    wrap = 2 * l + 2 * w
    bow = l * w * h
    ribbon = wrap + bow

    return (paper, ribbon)


def main():
    os.chdir(Path(__file__).parent)
    with open("day_02_2015_input.txt", "r") as infile:
        data = [line.strip() for line in infile.readlines()]

    total_paper, total_ribbon = 0, 0
    for gift in data:
        paper, ribbon = paper_and_ribbon(gift)
        total_paper += paper
        total_ribbon += ribbon

    print(total_paper)
    print(total_ribbon)


if __name__ == "__main__":
    main()
