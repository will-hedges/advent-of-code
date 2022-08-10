# day_01_2015.py - https://adventofcode.com/2015/day/1


def not_quite_lisp(data):
    floor = 0
    data = tuple(data)
    for index, char in enumerate(data):
        if char == "(":
            floor += 1
        else:
            floor -= 1
            if floor < 0:
                return index + 1
    return floor


"""
def not_quite_lisp(data):
    a = data.count("(")
    b = data.count(")")
    print(a - b)
"""


def main():
    with open("D:/Documents/python_projects/advent of code/2015/day_01_2015_input.txt", "r") as infile:
        data = infile.read()
    print(not_quite_lisp(data))


if __name__ == "__main__":
    main()
