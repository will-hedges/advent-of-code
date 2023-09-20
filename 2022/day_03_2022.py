import os
from pathlib import Path


def priority_value(item):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(item) + 1


def find_item_in_both_compartments(rucksack):
    possible_items = [item for item in rucksack if rucksack.count(item) >= 2]
    divider = len(rucksack) // 2
    compartment1, compartment2 = rucksack[:divider], rucksack[divider:]
    for item in possible_items:
        if item in compartment1 and item in compartment2:
            return priority_value(item)


def find_badge(group):
    group.sort(key=len)
    elf1, elf2, elf3 = group
    for item in elf1:
        if item in elf2 and item in elf3:
            return priority_value(item)


def part_one(rucksacks):
    priority_sum = 0

    for ruck in rucksacks:
        priority_sum += find_item_in_both_compartments(ruck)
    return priority_sum


def part_two(rucksacks):
    priority_sum = 0

    groups = [rucksacks[i : i + 3] for i in range(0, len(rucksacks), 3)]
    for group in groups:
        priority_sum += find_badge(group)

    return priority_sum


def main():
    os.chdir(Path(__file__).parent)
    rucksacks = []
    with open("day_03_2022.txt", "r") as infile:
        rucksacks = [line.strip() for line in infile.readlines()]

    print(part_one(rucksacks))  # 7568
    print(part_two(rucksacks))  # 2780


if __name__ == "__main__":
    main()
