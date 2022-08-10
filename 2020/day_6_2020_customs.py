#! python3
# day_6_2020.py


import os
from pathlib import Path


os.chdir(Path(__file__).parent)


#! python3
with open('day_6_2020.txt', 'r') as infile:
    questions = infile.read().split('\n\n')

any_yes = 0
for group in questions:
    any_yes += len(set(group.replace('\n', '')))

print(any_yes) # 7128 was my answer

all_yes = 0
for group in questions:
    passengers = group.split('\n')
    for answer in passengers[0]:
        yesses = [answer for passenger in passengers if answer in passenger]
        if len(yesses) == len(passengers):
            all_yes += 1

print(all_yes) # 3640 was my answer
