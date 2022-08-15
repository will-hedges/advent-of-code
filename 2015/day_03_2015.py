# day_03_2015.py - https://adventofcode.com/2015/day/3


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

    # part one
    sleigh = Sleigh()
    for direction in data:
        sleigh.move(direction)
    print(len(set(sleigh.coords)))
    
    # part two
    santa = Sleigh()
    robo = Sleigh()
    for index, direction in enumerate(data):
        if index % 2 == 0:
            santa.move(direction)
        else:
            robo.move(direction)

    all_coords = santa.coords + robo.coords
    print(len(set(all_coords)))


if __name__ == "__main__":
    main()
