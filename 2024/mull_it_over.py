#!/usr/bin/env python3
# mull_it_over.py - AoC 2024 Day 3 https://adventofcode.com/2024/day/3


import re


def get_sum_of_mulitplications(memory_lines):
    res = 0
    mul_re = re.compile(r"(mul\(\d*,\d*\))")

    for line in memory_lines:
        mo = re.findall(mul_re, line)
        # get a list of lists of the numbers, but they are still strings here
        #   could convert to ints with a map function but that is hard to read
        str_pairs = [match[4:].replace(")", "").split(",") for match in mo]
        for pair in str_pairs:
            a, b = pair
            res += int(a) * int(b)
    return res


def main():
    with open("mull_it_over_input.txt", "r") as infile:
        data = [line.strip() for line in infile.readlines()]

    # part one
    print(get_sum_of_mulitplications(data))  # 196826776
    return


if __name__ == "__main__":
    main()
