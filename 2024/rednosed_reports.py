#!/usr/bin/env python3
# rednosed_reports.py - AoC 2024 Day 02 https://adventofcode.com/2024/day/2


def get_level_changes(report):
    changes = []
    for i, v in enumerate(report):
        try:
            j = i + 1
            w = report[j]
            changes.append(v - w)
        except IndexError:
            break
    return changes


def count_safe_reports(data):
    count = 0
    for report in data:
        changes = get_level_changes(report)
        # check to see if all changes are negative or positive
        all_negative = all([x <= 0 for x in changes])
        all_positive = all([x >= 0 for x in changes])
        if all_negative or all_positive:
            # then check to see if they're all between 1 and 3\
            magnitude_check = all([1 <= abs(x) <= 3 for x in changes])
            if magnitude_check:
                count += 1

    return count


def count_safe_reports_with_problem_dampener(data):
    count = 0
    for report in data:
        # really need to get the index of the "bad" level
        # and then look to see if
        changes = get_level_changes(report)
        neg = [x <= 0 for x in changes].count(False)
        pos = [x >= 0 for x in changes].count(False)
        mag = [1 <= abs(x) <= 3 for x in changes].count(False)
        if neg + mag <= 1 or pos + mag <= 1:
            count += 1

    # NOTE: NOT YET SOLVED
    return count


def main():
    reports = []
    with open("rednosed_reports_input.txt", "r") as infile:
        for line in infile.readlines():
            report = [int(level) for level in line.strip().split(" ")]
            reports.append(report)

    # part one
    print(count_safe_reports(reports))  # 230
    # part two
    # 305 too high
    print(count_safe_reports_with_problem_dampener(reports))


if __name__ == "__main__":
    main()
