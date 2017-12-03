#!/usr/bin/env python3
"""
AoC solution day one
2017-12-01
"""

def sum_repeats(data_number, lag):
    """
    sum of the repeats ...
    """
    first = data_number[0:lag]
    second = data_number[lag:len(data_number)]
    lagged = second + first
    repeats = [(int(y) if (x == y) else 0) for x, y in zip(lagged, data_number)]
    total = sum(repeats)
    print(total)
    return total  # returning it so it can be tested

if __name__ == '__main__':
    with open('data/input_data.txt', 'r') as f:
        input_string = f.read().rstrip()
        sum_repeats(input_string, 1)
        sum_repeats(input_string, int(len(input_string) / 2))
