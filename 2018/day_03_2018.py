#!/usr/bin/env python3
# day_03_2018.py - https://adventofcode.com/2018/day/3

import re


def get_all_coords_in_grid(claim):
    x, y, dx, dy = claim
    coords = []
    # create each row
    for i in range(y, y + dy):
        for j in range(x, x + dx):
            coords.append((j, i))
    return coords


def get_all_overlapping_coords(puzzle):
    claim_re = re.compile(r"#\d+\s@\s(\d+),(\d+):\s(\d+)x(\d+)")

    claims = []
    for claim in puzzle:
        claim_mo = re.match(claim_re, claim)
        x, y, dx, dy = [int(n) for n in claim_mo.groups()]
        # note that in the example, the visualization is zero-indexed
        # so we need to add one to the starting coordinate
        claims.append([x + 1, y + 1, dx, dy])

    coords = []
    for claim in claims:
        grid = get_all_coords_in_grid(claim)
        coords += grid

    count = 0
    for coord in set(coords):
        if coords.count(coord) > 1:
            count += 1

    return count


def main():
    with open("input.txt", "r") as fo:
        puzzle = [x.strip() for x in fo.readlines()]

    # NOTE this should work for part 1 but takes too long
    part_one = get_all_overlapping_coords(puzzle)
    print(part_one)

    return


if __name__ == "__main__":
    main()
