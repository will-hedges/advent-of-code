def main():
    # split the puzzle input on double line break
    with open("input01.txt") as infile:
        data = infile.read().split("\n\n")
    # split up each sub "list" on \n and sum up the total of the list
    for i, v in enumerate(data):
        data[i] = sum([int(n) for n in v.split("\n") if n])
    # get the max
    print(max(data))
    # get the top 3 and sum
    print(sum(sorted(data, reverse=True)[:3]))


if __name__ == "__main__":
    main()
