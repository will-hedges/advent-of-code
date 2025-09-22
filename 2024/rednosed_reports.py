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


def check_report_safety(changes):
    if all([delta <= 0 for delta in changes]) or all([delta >= 0 for delta in changes]):
        if all([1 <= abs(delta) <= 3 for delta in changes]):
            return True
    return False


def count_safe_reports(data):
    count = 0
    for report in data:
        changes = get_level_changes(report)
        report_is_safe = check_report_safety(changes)
        if report_is_safe:
            count += 1

    return count


def count_safe_reports_with_problem_dampener(data):
    count = 0
    for report in data:
        changes = get_level_changes(report)
        neg = [x <= 0 for x in changes]
        pos = [x >= 0 for x in changes]
        mag = [1 <= abs(x) <= 3 for x in changes]
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
