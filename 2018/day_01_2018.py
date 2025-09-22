#!/usr/bin/env python3
# day_01_2018.py - https://adventofcode.com/2018/jday/1


from itertools import accumulate, cycle


def find_first_repeated_frequency(frequency_changes):
    # start with a blank set for 0 starting cases
    seen = set({0})
    # calculate each new frequency with cycle and accumulate
    for f in accumulate(cycle(frequency_changes)):
        # if the new frequency is already in the set, this is our answer
        # otherwise, add it to the set and keep going
        if f in seen:
            return f
        else:
            seen.add(f)

    return


def main():
    with open("input.txt", "r") as fo:
        frequency_changes = [int(x) for x in fo.readlines()]

    part_one = sum(frequency_changes)
    print(part_one)

    part_two = find_first_repeated_frequency(frequency_changes)
    print(part_two)

    return


if __name__ == "__main__":
    main()
