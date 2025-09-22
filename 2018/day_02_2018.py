#!/usr/bin/env python3
# day_02_2018.py - https://adventofcode.com/2018/day/2


def get_exactly_n(puzzle, n):
    res = 0
    for line in puzzle:
        line_set = set(line)
        line_dict = {k: line.count(k) for k in line_set if line.count(k) == n}
        if line_dict.keys():
            res += 1
        pass

    return res


def get_checksum(puzzle):
    twos = get_exactly_n(puzzle, 2)
    threes = get_exactly_n(puzzle, 3)
    checksum = twos * threes
    return checksum


def find_correct_box_ids(puzzle):
    for i, x in enumerate(puzzle):
        for j, y in enumerate(puzzle[i + 1 :]):
            res = 0
            for a, b in zip(x, y):
                if a != b:
                    res += 1

            if res == 1:
                return (x, y)

    return


def get_common_letters_between_box_ids(id1, id2):
    res = []
    for a, b in zip(id1, id2):
        if a == b:
            res.append(a)

    return "".join(res)


def main():
    with open("input.txt", "r") as fo:
        puzzle = [x.strip() for x in fo.readlines()]

    part_one = get_checksum(puzzle)
    print(part_one)  # 5952

    id1, id2 = find_correct_box_ids(puzzle)
    part_two = get_common_letters_between_box_ids(id1, id2)
    print(part_two)  # krdmtuqjgwfoevnaboxglzjph

    return


if __name__ == "__main__":
    main()
