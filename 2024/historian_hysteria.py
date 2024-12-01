#!/usr/bin/env python3
# historian_hysteria.py - Advent of Code 2024 Day 1 https://adventofcode.com/2024/day/1


def compare_list_distances(left_list, right_list):
    return sum([abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list))])


def similarity_score(left_list, right_list):
    score = 0
    for i in left_list:
        score += i * right_list.count(i)
    return score


def main():
    left_list, right_list = [], []

    with open("historian_hysteria.txt", "r") as infile:
        data = [line.strip().split("   ") for line in infile.readlines()]

    for sublist in data:
        l, r = sublist
        left_list.append(int(l))
        right_list.append(int(r))

    part_one = compare_list_distances(left_list, right_list)
    print(part_one)

    part_two = similarity_score(left_list, right_list)
    print(part_two)

    return


if __name__ == "__main__":
    main()
