#! python3
# day_11_2020.py

import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
os.chdir(Path(__file__).parent)


#! python3
with open('seats.txt', 'r') as infile:
    rows = [list(line.strip()) for line in infile.readlines()]

# 1 2 3
# 8 L 4
# 7 6 5
for idx, row in enumerate(rows):
    for i, spot in enumerate(row):
        if spot == 'L':
            adj_seats = []
            try:
                one = rows[idx-1][i - 1]
                adj_seats.append(one)
            except IndexError:
                pass
            try:
                two = rows[idx-1][i]
                adj_seats.append(two)
            except IndexError:
                pass
            try:
                three = rows[idx-1][i+1]
                adj_seats.append(three)
            except IndexError:
                pass
            try:
                four = rows[idx][i+1]
                adj_seats.append(four)
            except IndexError:
                pass
            try:
                five = rows[idx+1][i+1]
                adj_seats.append(five)
            except IndexError:
                pass
            try:
                six = rows[idx+1][i]
                adj_seats.append(six)
            except IndexError:
                pass
            try:
                seven = rows[idx+1][i-1]
                adj_seats.append(seven)
            except IndexError:
                pass
            try:
                eight = rows[idx][i-1]
                adj_seats.append(eight)
            except IndexError:
                pass

            if adj_seats.count('#') < 4:
                row[i] = '#'


for row in rows:
    print(''.join(row))