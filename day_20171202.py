#!/usr/bin/env python3
"""
"""

import csv

# Part one
def max_min_row(input_csv):
    """
    """
    diffs = []
    for row in input_csv:
        diff = max(row) - min(row)
        diffs.append(diff)
        return diffs

def checksum(input_csv):
    """
    """
    diffs = max_min_row(input_csv)
    return sum(diffs)


# Part two
def find_pairs_division(row):
    """
    """
    row.sort(reverse=True)
    div = [int(num / den) for i, num in enumerate(row) for den in row[i + 1:len(row)] if num % den == 0]
    return div

def divisions(input_csv):
    """
    """
    divs = []
    for row in input_csv:
        div = find_pairs_division(row)
        divs += div
        return divs

def checksum_div(input_csv):
    """
    """
    divs = divisions(input_csv)
    return sum(divs)


if __name__ == '__main__':
    with open('data/input_data_20171202.csv', 'r') as csvfile:
        input = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        print(checksum(input))
        csvfile.seek(0)  # to reset the reader row pointer
        print(checksum_div(input))
