#!/usr/bin/env python

import os
from pathlib import Path


class Submarine():
    def __init__(self):
        self.x, self.y, self.a = 0, 0, 0
        return
    
    def part_one_move(self, cmd):
        direction, value = cmd
        if direction == 'forward':
            self.x += value
        elif direction == 'up':
            self.y -= value
        elif direction == 'down':
            self.y += value
        return
    
    def part_two_move(self, cmd):
        direction, value = cmd
        if direction == 'forward':
            self.x += value
            self.y += self.a * value
        elif direction == 'up':
            self.a -= value
        elif direction == 'down':
            self.a += value
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
        submarine.part_one_move(cmd)
    part_one_ans = submarine.x * submarine.y
    print(part_one_ans)

    submarine = Submarine()
    for cmd in cmds:
        submarine.part_two_move(cmd)
    part_two_ans = submarine.x * submarine.y
    print(part_two_ans)
    return


if __name__ == "__main__":
    main()
