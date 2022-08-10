#! python3
# day_7_2020.py


import logging
import os
from pathlib import Path


logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
os.chdir(Path(__file__).parent)


import re


inner_re = re.compile(r'(\d) (\w+ \w+) bags?')
outer_re = re.compile(r'(.+) bags contain (.+)')

#! python3
with open('bag_rules.txt', 'r') as infile:
    rules = infile.read()

bag_dic = {
    bag:
        {content: int(n) for n, content in inner_re.findall(contents)}
            for bag, contents in outer_re.findall(rules)
    }

bag_lst = [color for color, contents in bag_dic.items() if 'shiny gold' in contents.keys()]
for bag in bag_lst:
    for color, contents in bag_dic.items():
        if bag in contents.keys():
            bag_lst.append(color)

print(len(set(bag_lst))) # 115

nested_bags = []


def count_bags(target_bag):
    global bag_dic
    global nested_bags

    sub_bags = bag_dic[target_bag]

    for bag in sub_bags:
        n = int(sub_bags[bag])
        for i in range(n):
            nested_bags.append(item for item in count_bags(bag))

    return nested_bags


print(len(count_bags('shiny gold'))) # 1250
