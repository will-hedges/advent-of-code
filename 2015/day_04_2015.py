# day_04_2015.py - https://adventofcode.com/2015/day/4

import hashlib


def find_lowest_number_hash(secret_key):
    for i in range(1_000_000):
        hash = hashlib.md5((secret_key + str(i).zfill(5)).encode("utf-8")).hexdigest()
        if hash.startswith("00000"):
            return i


def main():
    # part one
    print(find_lowest_number_hash("ckczppom"))


if __name__ == "__main__":
    main()
