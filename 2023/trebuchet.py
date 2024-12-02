#!/usr/bin/env python3
# trebuchet.py - Advent of Code 2023 Day 01 https://adventofcode.com/2023/day/1

import re


def get_sum_of_calibration_values(document):
    calibration_value_sum = 0
    for line in document:
        digit_tups = []
        for x in line:
            try:
                int(x)
                digit_tups.append(x)
            except ValueError:
                pass

        a, b = digit_tups[0], digit_tups[-1]
        calibration_value = int(a + b)
        calibration_value_sum += calibration_value

    return calibration_value_sum


def get_indices_of_all_values(document):
    calibration_value_sum = 0
    digit_tups = (
        ("1", "one"),
        ("2", "two"),
        ("3", "three"),
        ("4", "four"),
        ("5", "five"),
        ("6", "six"),
        ("7", "seven"),
        ("8", "eight"),
        ("9", "nine"),
    )

    for line in document:
        mapped_digits = []
        for digit in digit_tups:
            num, alpha = digit
            num_idx = [i.start() for i in re.finditer(num, line)]
            alpha_idx = [j.start() for j in re.finditer(alpha, line)]
            idxs = sorted(num_idx + alpha_idx)

            if idxs:
                mapped_digits.append((num, idxs))

        # get the first digit ('num') that appears in the list, sorted by first
        #   value in the accompanying list, call it 'a'
        # then reverse that logic to get 'b'
        a = sorted(mapped_digits, key=lambda x: x[1][0] if x[1] else float("inf"))[0][0]
        b = sorted(
            mapped_digits,
            key=lambda x: max(x[1]) if x[1] else float("-inf"),
            reverse=True,
        )[0][0]

        calibration_value_sum += int(a + b)

    return calibration_value_sum


def main():
    with open("trebuchet_input.txt", "r") as infile:
        calibration_document = [line.strip() for line in infile.readlines()]

    # NOTE part 1 function does not work with part 2 input
    # print(get_sum_of_calibration_values(calibration_document))  # 54990
    print(get_indices_of_all_values(calibration_document))  # 54473

    return


if __name__ == "__main__":
    main()
