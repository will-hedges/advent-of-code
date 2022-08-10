#! python3
# day_18_2020_operations.py
import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
os.chdir(Path(__file__).parent)


#! python3
with open('operations_test.txt', 'r') as infile:
# with open('math.txt', 'r') as infile:
    homeworkLines = [line.strip() for line in infile.readlines()]

logging.debug(f'homeworkLines == {homeworkLines}')

for eqn in homeworkLines:
    eqn = eqn.split(' ')

    logging.debug(f'eqn == {eqn}')