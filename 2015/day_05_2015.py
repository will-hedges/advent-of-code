# day_05_2015.py - https://adventofcode.com/2015/day/5


import os
from pathlib import Path


def bool_double_letter(s):
    for char1, char2 in zip(s[::2], s[1::2]):
        if char1 == char2:
            return True
    return False


def count_nice_strings(data):
    nice = 0
    for s in data:
        three_vowels = sum(s.count(vowel) for vowel in "aeiou")
        double_letter = bool_double_letter(s)
        no_bad_combos = not any(
            [
                "ab" in s,
                "cd" in s,
                "pq" in s,
                "xy" in s

            ]
        )
        if all([three_vowels, double_letter, no_bad_combos]):
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
