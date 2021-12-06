#!/usr/bin/env python

import os
from pathlib import Path


def get_gamma_rate(data):
    n = len(data[0])
    gamma_rate = ''
    for i in range(n):
        bits = [s[i] for s in data]
        if bits.count('1') > bits.count('0'):
            gamma_rate += '1'
        else:
            gamma_rate += '0'
    return gamma_rate


def complement(s):
    return ''.join(['1' if x == '0' else '0' for x in list(s)])


def bit_filter(data, pref):
    n = len(data[0])
    for i in range(n):
        bits = [s[i] for s in data]
        if bits.count('1') >= bits.count('0'):
            data = [s for s in data if s[i] == pref]
        else:
            data = [s for s in data if s[i] != pref]
        if len(data) == 1:
            return data.pop()
    

def main():
    os.chdir(Path(__file__).parent)
    with open('day_03_2021_input.txt', 'r') as f:
        diagnostic_report = [line.strip() for line in f.readlines()]

    gamma_rate = get_gamma_rate(diagnostic_report)
    epsilon_rate = complement(gamma_rate)
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(power_consumption)

    o2_rating = bit_filter(diagnostic_report, '1')
    co2_rating = bit_filter(diagnostic_report, '0')
    life_support_rating = int(o2_rating, 2) * int(co2_rating, 2)
    print(life_support_rating)


if __name__ == "__main__":
    main()