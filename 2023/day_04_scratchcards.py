#!/usr/bin/env python3
# day_04_scratchcards.py - https://adventofcode.com/2023/day/4


from scratchcard import Scratchcard


def main():
    with open("input.txt", "r") as fo:
        cards = fo.readlines()

    pile_worth = 0
    for card in cards:
        sc = Scratchcard(card)
        pile_worth += sc.worth

    # part one
    print(pile_worth)

    return


if __name__ == "__main__":
    main()
