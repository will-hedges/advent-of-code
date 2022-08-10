#! python3
# day_two_2019.py

import os
from pathlib import Path


os.chdir(Path(__file__).parent)
with open('day_2_2019.txt', 'r') as infile:
    input_lst = [int(n) for n in infile.read().split(',')]


def part_one(lst, noun, verb):
    lst = lst.copy()
    lst[1], lst[2] = noun, verb
    i = 0
    while True:
        try:
            j, k, l, m = lst[i], lst[i+1], lst[i+2], lst[i+3]
            if j == 1:
                s = lst[k] + lst[l]
                lst[m] = s
            elif j == 2:
                p = lst[k] * lst[l]
                lst[m] = p
            elif j == 99:
                return lst
        except IndexError:
            return None

        i += 4


def part_two():
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = part_one(input_lst, noun, verb)[0]
            if result == 19690720:
                return 100 * noun + verb


print(f'Part One: {part_one(input_lst, 12, 2)[0]}') # 6087827
print(f'Part Two: {part_two()}') # 5379
