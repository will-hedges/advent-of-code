# day_05_2015.py - https://adventofcode.com/2015/day/5


import os
from pathlib import Path


def count_nice_strings(data):
    nice = 0
    for s in data:
        vowels = [s.count(vowel) for vowel in "aeiou"]
        if sum(vowels) >= 3:
            double_letters = [char * 2 in s for char in "abcdefghijklmnopqrstuvwxyz"]
            if any(double_letters):
                bad_combos = [
                        "ab" in s,
                        "cd" in s,
                        "pq" in s,
                        "xy" in s
                    ]
                if not any(bad_combos):
                    nice += 1
    return nice


def main():
    test_file = (
        "ugknbfddgicrmopn",
        "aaa",
        "jchzalrnumimnmhp",
        "haegwjzuvuyypxyu",
        "dvszwmarrgswjxmb",
    )
    os.chdir(Path(__file__).parent)
    with open("day_05_2015_input.txt", "r") as infile:
        data = [line.strip() for line in infile.readlines()]
        # data = test_file

    print(count_nice_strings(data))
    # 210 too low

if __name__ == "__main__":
    main()
