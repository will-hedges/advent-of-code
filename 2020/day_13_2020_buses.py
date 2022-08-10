#! python3
# day_13_2020.py
import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
os.chdir(Path(__file__).parent)


# with open('bus_test.txt', 'r') as infile:
with open('timetable.txt', 'r') as infile:
    timestamp = int(infile.readline())
    bus_ids = [int(n) for n in infile.readline().split(',') if n != 'x']

wait_times = [bus * (timestamp // bus) + bus - timestamp for bus in bus_ids]

part_one = bus_ids[wait_times.index(min(wait_times))] * min(wait_times) # 1915
print(part_one)
