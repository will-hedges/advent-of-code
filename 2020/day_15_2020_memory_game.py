#! python3
# day_15_2020.py
import logging
import os
from pathlib import Path
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
os.chdir(Path(__file__).parent)


#! python3
starting_nums = [2, 0, 1, 9, 5, 19]


def memory_game(lst, turns):

    dic = {num: turn for turn, num in enumerate(lst, start=1)}
    turn = len(lst) + 1
    num_to_speak = 0 # determine the first number to "play"

    while turn <= turns:
        lst.append(num_to_speak)

        if num_to_speak in dic.keys():
            next_num = turn - dic[num_to_speak]
            dic[num_to_speak] = turn
            num_to_speak = next_num

        else:
            dic[num_to_speak] = turn
            num_to_speak = 0

        turn += 1

    return lst[-1]


print(memory_game(starting_nums, 30000000))
