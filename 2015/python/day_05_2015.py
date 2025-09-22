# day_05_2015.py - https://adventofcode.com/2015/day/5


import os
from pathlib import Path


alphabet = "abcdefghijklmnopqrstuvwxyz"


def part_one(data):
    nice_strings = 0
    for s in data:
        vowels = [s.count(vowel) for vowel in "aeiou"]
        if sum(vowels) >= 3:
            global alphabet
            double_letters = [char * 2 in s for char in alphabet]
            if any(double_letters):
                bad_combos = [
                        "ab" in s,
                        "cd" in s,
                        "pq" in s,
                        "xy" in s
                    ]
                if not any(bad_combos):
                    nice_strings += 1
    return nice_strings


def part_two(data):
    nice_strings = 0

            

def main():
    test_file = (
        "qjhvhtzxzqqjkmpb",
        "xxyxx",
        "uurcxstgmygtbstg",
        "ieodomkazucvgmuy",
    )
    os.chdir(Path(__file__).parent)
    with open("day_05_2015_input.txt", "r") as infile:
        # data = [line.strip() for line in infile.readlines()]
        data = test_file

    print(part_one(data))
    
    print(part_two(data))

if __name__ == "__main__":
    main()
