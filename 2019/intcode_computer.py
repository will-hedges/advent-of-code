#!/usr/bin/env python3
# intcode_computer.py - a Python class representing an Intcode computer


class Intcode_Computer:
    def __init__(self, instructions):
        self.instructions = instructions
        return

    def run_instructions(self, noun=12, verb=2):
        intcode_output = self.instructions
        intcode_output[1:3] = noun, verb

        i = 0
        while True:
            try:
                j, k, l, m = intcode_output[i : i + 4]
                if j == 1:
                    s = intcode_output[k] + intcode_output[l]
                    intcode_output[m] = s
                elif j == 2:
                    p = intcode_output[k] * intcode_output[l]
                    intcode_output[m] = p
                elif j == 99:
                    self.intcode_output = intcode_output[0]
                    return
            except IndexError:
                self.intcode_output = intcode_output[0]
                return
            i += 4

    def find_noun_and_verb_that_output(self, target):
        for noun in range(0, 100):
            for verb in range(0, 100):
                self.run_instructions(noun, verb)
                if self.intcode_output == target:
                    self.noun = noun
                    self.verb = verb
                    return

