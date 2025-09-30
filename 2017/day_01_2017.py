#!/usr/bin/env python3
# day_01_2017.py - https://adventofcode.com/2017/day/1


def inverse_captcha(seq):
    res = 0
    for i, v in enumerate(seq):
        try:
            w = seq[i + 1]
        except IndexError:
            w = seq[0]
        if int(v) == int(w):
            res += v
    return res


def inverse_captcha2(seq):
    res = 0
    jump = len(seq) // 2

    for i, v in enumerate(seq):
        try:
            w = seq[i + jump]
        except IndexError:
            j = i + jump - len(seq)
            w = seq[j]

        if int(v) == int(w):
            res += v
    return res


def main():
    with open("input.txt", "r") as fo:
        seq = [int(x) for x in fo.read()]

    part_one = inverse_captcha(seq)
    print(part_one)

    part_two = inverse_captcha2(seq)
    print(part_two)

    return


if __name__ == "__main__":
    main()
