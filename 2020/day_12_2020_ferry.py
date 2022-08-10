#! python3
# day_12_2020.py
import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
os.chdir(Path(__file__).parent)


import re


action_re = re.compile(r'([NSWELRF])(\d+)')

with open('ferry_actions.txt', 'r') as infile:
    actions = [action_re.search(line) for line in infile.readlines()]


class Ferry():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.r = 0
        self.wx = 10
        self.wy = 1


    def move_ferry_cardinal(self, direction, units):
        if direction == 'N':
            self.y += units
        elif direction == 'S':
            self.y -= units
        elif direction == 'W':
            self.x -= units
        elif direction == 'E':
            self.x += units


    def move_ferry_forward(self, units):
        if self.r == 0:
            self.x += units
        elif self.r == 90:
            self.y -= units
        elif self.r == 180:
            self.x -= units
        elif self.r == 270:
            self.y += units


    def turn_ferry(self, direction, degrees):
        if direction == 'L':
            degrees *= -1
        self.r += degrees
        self.r %= 360


    def move_waypoint_cardinal(self, direction, units):
        if direction == 'N':
            self.wy += units
        elif direction == 'S':
            self.wy -= units
        elif direction == 'W':
            self.wx -= units
        elif direction == 'E':
            self.wx += units


    def move_toward_waypoint(self, times):
        self.x += self.wx * times
        self.y += self.wy * times


    def rotate_waypoint(self, direction, degrees):
        if direction == 'L':
            degrees = 360 - degrees

        if degrees == 90:
            self.wx, self.wy = self.wy, self.wx * -1
        elif degrees == 180:
            self.wx *= -1
            self.wy *= -1
        elif degrees == 270:
            self.wx, self.wy = self.wy * -1, self.wx


def part_one(action_lst):
    ferry = Ferry()

    for action in action_lst:
        mvmt = action.group(1)
        dist = int(action.group(2))
        if mvmt in 'NSWE':
            ferry.move_ferry_cardinal(mvmt, dist)
        elif mvmt == 'F':
            ferry.move_ferry_forward(dist)
        elif mvmt in 'LR':
            ferry.turn_ferry(mvmt, dist)

    return abs(ferry.x) + abs(ferry.y)


def part_two(action_lst):
    ferry = Ferry()

    for action in action_lst:
        mvmt = action.group(1)
        dist = int(action.group(2))
        if mvmt in 'NSWE':
            ferry.move_waypoint_cardinal(mvmt, dist)
        elif mvmt == 'F':
            ferry.move_toward_waypoint(dist)
        elif mvmt in 'LR':
            ferry.rotate_waypoint(mvmt, dist)

    return abs(ferry.x) + abs(ferry.y)


print(part_one(actions)) # 1106
print(part_two(actions)) # 107281
