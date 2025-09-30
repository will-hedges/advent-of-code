#! python3
# day_02_2019.py - https://adventofcode.com/2019/day/2


from intcode_computer import Intcode_Computer


def main():
    with open("input.txt", "r") as infile:
        instructions = [int(n) for n in infile.read().split(",")]

    ic = Intcode_Computer(instructions)

    ic.run_instructions()
    part_one = ic.intcode_output
    print(part_one)

    ic.find_noun_and_verb_that_output(19690720)
    part_two = 100 * ic.noun + ic.verb
    print(part_two)

    return


if __name__ == "__main__":
    main()
