#! python3
# day_8_2020.py

# my answers are apparently 216 and 509 but I have no idea how this DOESN'T work
import os
from pathlib import Path


os.chdir(Path(__file__).parent)


boot_codes = []
with open('boot_code.txt', 'r') as infile:
    for line in infile.readlines():
        line = line.strip().split()
        op = line[0]
        val = int(line[1])
        boot_codes.append([op, val])


def part_one(bootcode):
    acc, idx = 0, 0
    idx_seen = []

    while True:
        op = bootcode[idx][0]
        val = bootcode[idx][1]

        if op == 'acc':
            acc += val
            idx += 1
        elif op == 'jmp':
            idx += val
        elif op == 'nop':
            idx += 1

        if idx in idx_seen:
            return acc
        else:
            idx_seen.append(idx)


print(part_one(boot_codes)) # 1501


def part_two(bootcode, idx_to_flip):
    acc, idx = 0, 0
    idx_seen = []

    while True:
        try:
            op = bootcode[idx][0]
            val = bootcode[idx][1]
        except IndexError:
            return acc

        if idx in idx_seen:
            return None
        else:
            idx_seen.append(idx)

        if idx == idx_to_flip:
            if op == 'jmp':
                op = 'nop'
            elif op == 'nop':
                op = 'jmp'

        if op == 'acc':
            acc += val
            idx += 1
        elif op == 'jmp':
            idx += val
        elif op == 'nop':
            idx += 1
        else:
            print(f'Unk val @ idx {idx}. Failed.')
            return None


i = 0
while True:
    op = boot_codes[i][0]
    if op == 'acc':
        i += 1
    else:
        ans = part_two(boot_codes, i)
        if ans is not None:
            print(ans)
            break
        else:
            i += 1
