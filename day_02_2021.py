#!/usr/bin/env python

import os
from pathlib import Path


class Submarine():
    def __init__(self):
        self.horizontal_position, self.depth, self.depth_by_aim, self.aim = 0, 0, 0, 0
        return
    
    def move(self, cmd):
        direction, value = cmd
        if direction == 'forward':
            self.horizontal_position += value
            self.depth_by_aim += self.aim * value
        elif direction == 'up':
            self.depth -= value
            self.aim -= value
        elif direction == 'down':
            self.depth += value
            self.aim += value
        return


def main():
    os.chdir(Path(__file__).parent)
    cmds = []
    # with open('test_input.txt', 'r') as f:
    with open('day_02_2021_input.txt', 'r') as f:
        for line in f.readlines():
            direction, value = line.split()
            cmds.append((direction, int(value)))
    
    submarine = Submarine()
    for cmd in cmds:
        submarine.move(cmd)
        
    part_one = submarine.horizontal_position * submarine.depth
    print(part_one)

    part_two = submarine.horizontal_position * submarine.depth_by_aim
    print(part_two)

    return


if __name__ == "__main__":
    main()
