#!/usr/bin/env python3
# mull_it_over.py - AoC 2024 Day 3 https://adventofcode.com/2024/day/3


import re


def get_sum_of_multiplications(memory_lines):
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


def find_all_indices_of_substring(sub, _str):
    start = 0
    while True:
        start = _str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


def handle_do_and_donts(memory_lines):
    res = 0
    # what if we index everything that is between do() and don't()?
    for line in memory_lines:
        dos = [0] + list(find_all_indices_of_substring("do()", line))
        donts = list(find_all_indices_of_substring("don't()", line)) + [len(line)]
        slice_idxs = [(a, b) for a, b in zip(dos, donts)]
        line_slices = []
        for tup in slice_idxs:
            start, stop = tup
            line_slices.append(line[start:stop])
        res += get_sum_of_multiplications(line_slices)
    return res


def main():
    with open("mull_it_over_input.txt", "r") as infile:
        data = [line.strip() for line in infile.readlines()]

    # part one
    print(get_sum_of_multiplications(data))  # 196826776

    # part two TODO SOLVE
    # 321615145 too high
    print(handle_do_and_donts(data))

    return


if __name__ == "__main__":
    main()
