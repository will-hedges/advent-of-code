# day_04_2015.py - https://adventofcode.com/2015/day/4

import hashlib


def find_lowest_number_hash(secret_key, n_leading_zeros):
    i = 0
    while True:
        hash = hashlib.md5((secret_key + str(i).zfill(n_leading_zeros)).encode("utf-8")).hexdigest()
        if hash.startswith("0" * n_leading_zeros):
            return i
        i += 1


def main():
    puzzle_key = "ckczppom"
    # part one
    print(find_lowest_number_hash(puzzle_key, 5))
    # part two
    print(find_lowest_number_hash(puzzle_key, 6))


if __name__ == "__main__":
    main()
