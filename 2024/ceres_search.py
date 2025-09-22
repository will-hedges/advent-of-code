#!/usr/bin/env python3
# ceres_search.py - AoC 2024 Day 4 https://adventofcode.com/2024/day/4


def find_all_indices_of_a_substring(string, substring):
    indices = []
    start_index = 0

    while True:
        start_index = string.find(substring, start_index)
        if start_index == -1:
            break
        indices.append(start_index)
        start_index += 1

    return indices


def count_all_occurences_of_a_substring(string, substring):
    return len(find_all_indices_of_a_substring(string, substring))


def count_xmas_in_word_search(rows):
    xmas_count = 0
    # get all the ones that are straight across or reverse
    for row in rows:
        xmas_count += count_all_occurences_of_a_substring(row, "XMAS")
        xmas_count += count_all_occurences_of_a_substring(row[::-1], "XMAS")

    # get all the up and down ones
    for i in range(len(row)):
        col = "".join([row[i] for row in rows])
        xmas_count += count_all_occurences_of_a_substring(col, "XMAS")
        xmas_count += count_all_occurences_of_a_substring(col[::-1], "XMAS")

    """ 
    start back at the top and search diagonals
    search indices like so - basically going to increment in the different
        directions and the just swap the indices
    [0,0] [0,1] [0,2]
    [1,0] [1,1] [1,2]
    ...
    """
    x = len(row)
    for i in range(len(row)):
        try:
            j, k = i + 1, i + 2
            diag, diag_top, diag_down = [rows[i][i]], [rows[i][j]], [rows[j][i]]

            while True:
                try:
                    diag.append(rows[j][j])
                    diag_top.append(rows[j][k])
                    diag_down.append(rows[k][j])
                    j += 1
                    k += 1
                except IndexError:
                    break

            diag = "".join(diag)
            diag_top = "".join(diag_top)
            diag_down = "".join(diag_down)

            for d in (diag, diag_top, diag_down):
                xmas_count += count_all_occurences_of_a_substring(d, "XMAS")
                xmas_count += count_all_occurences_of_a_substring(d[::-1], "XMAS")

        except IndexError:
            break

    return xmas_count


def main():
    with open("ceres_search_input.txt", "r") as infile:
        data = [line.strip() for line in infile.readlines()]

    # part one
    # 2149 too low
    print(count_xmas_in_word_search(data))
    return


if __name__ == "__main__":
    main()
