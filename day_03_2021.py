#!/usr/bin/env python

import os
from pathlib import Path


def get_gamma_rate(data):
    gamma_rate = ''
    for i in range(len(data[0])):
        bits = [s[i] for s in data]
        if bits.count('1') > bits.count('0'):
            gamma_rate += '1'
        else:
            gamma_rate += '0'
    return gamma_rate


def complement(s):
    return ''.join(['1' if x == '0' else '0' for x in list(s)])


def get_life_support_rating(data):
    n = len(data[0])

    o2_rating = data.copy()
    for i in range(n):
        bits = [s[i] for s in o2_rating]
        if bits.count('1') >= bits.count('0'):
            o2_rating = [s for s in o2_rating if s[i] == '1']
        else:
            o2_rating = [s for s in o2_rating if s[i] == '0']
        if len(o2_rating) == 1:
            break

    co2_rating = data.copy()
    for i in range(n):
        bits = [s[i] for s in co2_rating]
        if bits.count('1') >= bits.count('0'):
            co2_rating = [s for s in co2_rating if s[i] == '0']
        else:
            co2_rating = [s for s in co2_rating if s[i] == '1']
        if len(co2_rating) == 1:
            break

    return int(o2_rating.pop(), 2) * int(co2_rating.pop(), 2)


def main():
    os.chdir(Path(__file__).parent)
    with open('day_03_2021_input.txt', 'r') as f:
        diagnostic_report = [line.strip() for line in f.readlines()]

    gamma_rate = get_gamma_rate(diagnostic_report)
    epsilon_rate = complement(gamma_rate)
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(power_consumption)

    print(get_life_support_rating(diagnostic_report))
    return


if __name__ == "__main__":
    main()