#!/usr/bin/env python

import os
from pathlib import Path


def move_crabs(crab_positions, incremental_cost_per_move):
    total_fuel_costs = []
    for crab1 in crab_positions:
        cost_of_move = []
        for crab2 in crab_positions:
            cost_per_move = 1
            cost_of_move.append()

def main():
    os.chdir(Path(__file__).parent)
    with open("test_input.txt", "r") as f:
    # with open("day_07_2021_input.txt", "r") as f:
        crab_positions = [int(n) for n in f.read().split(",")]
    
    # part 1
    total_fuel_costs = []
    for crab1 in crab_positions:
        total_fuel_costs.append(sum([abs(crab1 - crab2) for crab2 in crab_positions]))
    cheapest_move = sorted(total_fuel_costs)[0]
    print(cheapest_move)

    # part 2
    total_fuel_costs = []
    for crab1 in crab_positions:
        for crab2 in crab_positions:
            print(f"move from {crab1} to {crab2}")
        print('new_crab')
    return


if __name__ == "__main__":
    main()
    