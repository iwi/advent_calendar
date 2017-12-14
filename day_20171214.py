#!/usr/bin/env python3
"""
AoC solution day 14
"""

import day_201712010 as dt
from functools import reduce


def build_input_strings(st):
    built_strings = []
    for i in range(128):
        built_strings.append(st + '-' + str(i))
    return built_strings


if __name__ == '__main__':
    input_string = 'nbysizxe'
    # input_string = 'flqrgnkx'
    input_strings = build_input_strings(input_string)
    hashed_rows = ['0x' + dt.hash(s) for s in input_strings]
    bin_rows = [bin(int(x, 16))[2:] for x in hashed_rows]
    suma = reduce(lambda i, bs: i + bs.count('1'), bin_rows, 0) 
    print(suma)


