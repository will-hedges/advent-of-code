#! python3
# day_10_2020.py


import os
from pathlib import Path


os.chdir(Path(__file__).parent)


# python3
with open('adapters.txt', 'r') as infile:
    adapters = sorted([int(n) for n in infile.readlines()])

adapters.insert(0, 0)
adapters.append(max(adapters) + 3)

delta_lst = []
for i, v in enumerate(adapters):
    try:
        delta_lst.append(abs(adapters[i] - adapters[i+1]))
    except IndexError:
        pass

delta_dic = {n: delta_lst.count(n) for n in set(delta_lst)}
print(delta_dic)
print(delta_dic[1] * delta_dic[3])