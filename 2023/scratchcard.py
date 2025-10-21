#!/usr/bin/env python3
# scratchcard.py - a Python class representing a scratch-off card


class Scratchcard:
    """
    A simple Python class representing a scratch-off card

    Props:
        id (int): the card number - Card '1', etc.
        worth (int): the scored value of the card
        matches (int): the number of playing numbers that match winning numbers
    """

    def __init__(self, numbers):
        # get card id, winning and playing numbers
        card_id, numbers = numbers.split(":")
        card_id = int(card_id.split(" ")[-1])
        winning, playing = numbers.split("|")

        # get lists of numbers as ints
        winning = [int(n) for n in winning.split(" ") if n]
        playing = [int(n) for n in playing.split(" ") if n]

        # figure out how many winning numbers you have and score the card
        matches = len([p for p in playing if p in winning])
        if matches <= 1:
            worth = matches
        else:
            worth = 2 ** (matches - 1)

        self.id = card_id
        self.worth = worth
        self.matches = matches
        return
