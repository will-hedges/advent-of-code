#!/usr/bin/env python3
# day_04_2019.py - https://adventofcode.com/2019/day/4


def password_meets_criteria(password):
    two_adj_digits = False
    for i in range(10):
        # added "nnn" condition for part two
        if f"{i}{i}" in password and f"{i}{i}{i}" not in password:
            two_adj_digits = True
            break

    if sorted(list(password)) == list(password):
        digits_never_decrease = True
    else:
        digits_never_decrease = False

    if all((two_adj_digits, digits_never_decrease)):
        return True
    return False


def count_valid_passwords(i, j):
    valid_passwords = 0
    for n in range(i, j + 1):
        valid_password = password_meets_criteria(str(n))
        if valid_password is True:
            valid_passwords += 1
    return valid_passwords


def main():
    with open("input.txt", "r") as fo:
        a, b = fo.read().split("-")

    i, j = int(a), int(b)
    res = count_valid_passwords(i, j)
    print(res)

    return


if __name__ == "__main__":
    main()
