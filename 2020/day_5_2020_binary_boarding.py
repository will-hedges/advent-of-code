#! python3
# day_5_2020.py


import os
from pathlib import Path
os.chdir(Path(__file__).parent)
# tickets = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL'] # 567, 119, 820


with open('day_5_2020.txt', 'r') as infile:
    tickets = [line.strip() for line in infile.readlines()]

seat_ids = []

for ticket in tickets:
    row, col = [i for i in range(128)], [i for i in range(8)]
    ticket_row, ticket_col = ticket[:7], ticket[7:]

    for x in ticket_row:
        if x == 'F':
            row = row[:len(row) // 2]
        elif x == 'B':
            row = row[len(row) // 2:]

    for y in ticket_col:
        l = len(col)
        if y == 'L':
            col = col[:len(col) // 2]
        elif y == 'R':
            col = col[len(col) // 2:]

    row, col = int(row.pop()), int(col.pop())
    seat_ids.append(row * 8 + col)

print(max(seat_ids)) # 998 !

missing_seats = [
    i for i in range(max(seat_ids) + 1)
        if i not in seat_ids
            and i + 1 in seat_ids
                and i - 1 in seat_ids
    ]
print(missing_seats.pop()) # 676 !
