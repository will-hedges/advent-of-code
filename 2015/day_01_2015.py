# day_01_2015.py - https://adventofcode.com/2015/day/1


import os
from pathlib import Path


def floors(data):
    floor = 0
    data = tuple(data)
    for index, char in enumerate(data):
        if char == "(":
            floor += 1
        else:
            floor -= 1
            if floor < 0:
                return index + 1
    return floor


def main():
    os.chdir(Path(__file__).parent)
    with open("day_01_2015_input.txt", "r") as infile:
        data = infile.read()
    print(floors(data))


if __name__ == "__main__":
    main() # 1783
