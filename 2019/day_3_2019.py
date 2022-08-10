#! python3
# day_3_2019.py

import os
from pathlib import Path
os.chdir(Path(__file__).parent)


import re


dir_re = re.compile(r'([UDLR])(\d{,3})')

with open('wires.txt', 'r') as infile:
# with open('wires_test.txt', 'r') as infile:
    input_lst = [line.strip().split(',') for line in infile.readlines()]

path1 = input_lst[0]
path2 = input_lst[1]


class Wire():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.step = 0
        self.pts = []


    def get_wire_coords(self, wire_path):
        coordinates = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        for segment in wire_path:
            mo = dir_re.search(segment)
            direction = mo.group(1)
            units = int(mo.group(2))

            dx, dy = coordinates[direction]
            for i in range(units):
                self.x += dx
                self.y += dy
                self.step += 1
                if (self.x, self.y) not in self.pts:
                    self.pts.append((self.x, self.y))

wire1 = Wire()
wire1.get_wire_coords(path1)

wire2 = Wire()
wire2.get_wire_coords(path2)

ix_pts = [p for p in wire1.pts if p in wire2.pts]

print(min([abs(x) + abs(y) for (x, y) in ix_pts]))
