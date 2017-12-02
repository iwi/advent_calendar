#!/usr/bin/env python3

import csv

# Part one
def max_min_row(input_csv):
    diffs = []
    for row in input_csv:
        diff = max(row) - min(row)
        diffs.append(diff)
    return(diffs)

def checksum(input_csv):
    diffs = max_min_row(input_csv)
    return(sum(diffs))


if __name__ == '__main__':
    with open('input_data_20171202.csv', 'r') as csvfile:
        input = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        print(checksum(input)) 
