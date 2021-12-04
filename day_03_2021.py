#!/usr/bin/env python

import os
from pathlib import Path


def power_consumption(lsts):
    gamma_rate = ''
    epsilon_rate = ''
    for x in range(len(lsts[0])):
        bits = [lst[x] for lst in lsts]
        i = bits.count('1')
        o = bits.count('0')
        if i > o:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def main():
    os.chdir(Path(__file__).parent)
    # with open('test_input.txt', 'r') as f:
    with open('day_03_2021_input.txt', 'r') as f:
        diagnostic_report = [list(line.strip()) for line in f.readlines()]
    print(power_consumption(diagnostic_report))


if __name__ == "__main__":
    main()