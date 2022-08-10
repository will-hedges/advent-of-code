#! python3
# day_16_2020.py


import logging
import os
from pathlib import Path


logging.basicConfig(level=logging.DEBUG, format=' %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)
os.chdir(Path(__file__).parent)


#! python3
import re


rule_re = re.compile(r'(\w+): (\d{,3})-(\d{,3}) or (\d{,3})-(\d{,3})')


with open('notes.txt', 'r') as infile:
# with open('ticket_scan.txt', 'r') as infile:
    raw_lst = infile.read().split('\n\n')

raw_lst = [strng.split('\n') for strng in raw_lst]

rules = raw_lst[0]
valid_lst, rule_dic = [], {}

for rule in rules:

    mo = rule_re.search(rule)
    name = mo.group(1)
    j, k = int(mo.group(2)), int(mo.group(3))
    x, y = int(mo.group(4)), int(mo.group(5))

    range_lst = [i for i in range(j, k + 1)] + [i for i in range(x, y + 1)]
    valid_lst += range_lst
    rule_dic[name] = range_lst

valid_set = set(valid_lst)

your_ticket = [int(n) for n in raw_lst[1].pop().split(',')]

nearby_tickets = [
    [int(n) for n in ticket.split(',')]
    for ticket in raw_lst[2][1:]
    ]


class Ticket_Data():

    def __init__(self):
        self.error_rate = 0
        self.valid_tickets = []


    def validate(self, tickets, valid_lst):
        for ticket in tickets:
            errors = [num for num in ticket if num not in valid_lst]
            if errors:
                self.error_rate += sum(errors)
            else:
                self.valid_tickets.append(ticket)


data = Ticket_Data()
data.validate(nearby_tickets, valid_set)

part_one = data.error_rate
print(part_one)


class Ticket():

    def __init__(self, nums):
        self.dic = {n: [] for n in nums}


    def find_meaning(self, rule_dic):

        for n in self.dic.keys():
            for idx, lst in enumerate(rule_dic.values()):
                if n in lst:
                    keys = list(rule_dic.keys())
                    self.dic[n].append(keys[idx])

        print(self.dic)

t = Ticket(nearby_tickets[0])

t.find_meaning(rule_dic)