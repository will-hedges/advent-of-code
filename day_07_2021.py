#!/usr/bin/env python

import os
from pathlib import Path


def main():
    os.chdir(Path(__file__).parent)
    # with open("test_input.txt", "r") as f:
    with open("day_07_2021_input.txt", "r") as f:
        crab_positions = [int(n) for n in f.read().split(",")]
    
    total_fuel_costs = []
    for crab1 in crab_positions:
        total_fuel_costs.append(sum([abs(crab1 - crab2) for crab2 in crab_positions]))
    cheapest_move = sorted(total_fuel_costs)[0]
    print(cheapest_move)

    return


if __name__ == "__main__":
    main()
    