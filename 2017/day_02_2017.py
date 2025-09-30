#!/usr/bin/env python3
# day_02_2017.py - https://adventofcode.com/2017/day/2


def calculate_checksum(spreadsheet):
    res = []
    for row in spreadsheet:
        res.append(max(row) - min(row))

    checksum = sum(res)
    return checksum


def worried_checksum(spreadsheet):
    res = []
    for row in spreadsheet:
        row.sort()
        # if we sort, the smaller values will be first
        # so we should divide w by v
        for i, v in enumerate(row):
            for w in row[i + 1 :]:
                if w % v == 0:
                    res.append(w // v)
                    break
    checksum = sum(res)
    return checksum


def main():
    spreadsheet = []
    with open("input.txt", "r") as fo:
        for line in fo.readlines():
            line = [int(x) for x in line.split()]
            spreadsheet.append(line)

    part_one = calculate_checksum(spreadsheet)
    print(part_one)

    part_two = worried_checksum(spreadsheet)
    print(part_two)

    return


if __name__ == "__main__":
    main()
