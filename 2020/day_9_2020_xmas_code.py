#! python3
# day_9_2020.py


import os
from pathlib import Path


os.chdir(Path(__file__).parent)

#! python3


with open('xmas_data.txt', 'r') as infile:
    xmas = [int(line) for line in infile.readlines()]


def find_outlier(data, p_len):
    valid_data = []
    for i, x in enumerate(data):
        try:
            preamble = data[i - p_len:i]
            for n in preamble:
                for m in preamble:
                    if n + m == x and x not in valid_data:
                        valid_data.append(x)
        except IndexError:
            pass

    return [x for x in data[p_len:] if x not in valid_data][0]


part_one = find_outlier(xmas, 25)
print(part_one) # 85848519


def find_contiguous_set(data, target_sum):
    for i, x in enumerate(data):
        total = x
        lst = [x]
        j = i + 1

        while total <= target_sum:
            total += data[j]
            lst.append(data[j])

            if total == target_sum:
                return min(lst) + max(lst)
            else:
                j += 1


part_two = find_contiguous_set(xmas, part_one)
print(part_two) # 13414198
