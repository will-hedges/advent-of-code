#!/usr/bin/env python

from itertools import islice
import os
from pathlib import Path


def replace_num_with_star(cards, num):
    new_cards = []
    for card in cards:
        new_card = []
        for row in card:
            new_row = [True if i == num else i for i in row]
            new_card.append(new_row)
        new_cards.append(new_card)
    return new_cards


def check_for_bingo(card_rows):
    bingo = [True] * 5
    card_cols = [row[i] for i in range(5) for row in card_rows]
    '''
    card_exes = [
        [card_rows[i][i] for i in range(5)],
        [card_rows[-i][-i] for i in range(1,6)]
    ]
    '''
    if bingo in card_rows or bingo in card_cols:
        return True
    return False


def main():
    os.chdir(Path(__file__).parent)
    # with open('test_input.txt', 'r') as f:
    with open('day_04_2021_input.txt', 'r') as f:
        Input = [line.strip() for line in f.read().split('\n') if line != '']
    drawn_numbers = [int(n) for n in Input.pop(0).split(',')]
    Inputt = iter(Input)
    Inputt = [list(islice(Inputt, elem)) for elem in [5] * (len(Input) // 5)]
    bingo_cards = []
    for card in Inputt:
        card = [[int(n) for n in row.replace("  ", " ").split()] for row in card]
        # consider using arrays...
        bingo_cards.append(card)
    
    bingo = False
    while bingo == False:
        n = drawn_numbers.pop(0)
        bingo_cards = replace_num_with_star(bingo_cards, n)
        for card in bingo_cards:
            bingo = check_for_bingo(card)
    
    uncalled_nums = []
    for row in card:
        for num in row:
            if num != True:
                uncalled_nums.append(num)
    
    # 2020 - too low
    part_one = sum(uncalled_nums) * n
    print(part_one)

    return
    

if __name__ == "__main__":
    main()
