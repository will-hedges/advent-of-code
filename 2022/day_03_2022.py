import os
from pathlib import Path


def get_priority_of_item_in_both_compartments(rucksack):
    priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    possible_items = [item for item in rucksack if rucksack.count(item) >= 2]
    divider = len(rucksack) // 2
    compartment1, compartment2 = rucksack[:divider], rucksack[divider:]
    for item in possible_items:
        if item in compartment1 and item in compartment2:
            return priorities.index(item) + 1


def part_one(rucksacks):
    priority_sum = 0
    for ruck in rucksacks:
        priority_sum += get_priority_of_item_in_both_compartments(ruck)
    return priority_sum


def main():
    os.chdir(Path(__file__).parent)
    rucksacks = []
    with open("day_03_2022.txt", "r") as infile:
        rucksacks = [line.strip() for line in infile.readlines()]

    print(part_one(rucksacks))  # 7568


if __name__ == "__main__":
    main()
