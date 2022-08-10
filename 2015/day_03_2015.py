# day_03_2015.py - https://adventofcode.com/2015/day/3


from collections import defaultdict
import os
from pathlib import Path


class Sleigh:
    def __init__(self):
        self.x, self.y = 0, 0
        self.coords = [(0, 0)]

    def move(self, arrow):
        if arrow == ">":
            self.x += 1
        elif arrow == "<":
            self.x -= 1
        elif arrow == "^":
            self.y += 1
        elif arrow == "v":
            self.y -= 1
        self.coords.append((self.x, self.y))


def main():
    os.chdir(Path(__file__).parent)
    with open("day_03_2015_input.txt", "r") as infile:
        data = tuple(infile.read())

    sleigh = Sleigh()
    for direction in data:
        sleigh.move(direction)
    # part one
    print(len(set(sleigh.coords)))
    # part two


if __name__ == "__main__":
    main()
