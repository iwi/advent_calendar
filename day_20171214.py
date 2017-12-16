#!/usr/bin/env python3
"""
AoC solution day 14
"""

import day_201712010 as dt
from functools import reduce
import numpy as np


def build_input_strings(st):
    built_strings = []
    for i in range(128):
        built_strings.append(st + '-' + str(i))
    return built_strings


def convert_filled_adjacent(row, col, bin_rows_list):
    if (row == len(bin_rows_list)) | (col == len(bin_rows_list[0])) | (col < 0) | (row < 0):
        return bin_rows_list

    if bin_rows_list[row][col] == '0':
        return bin_rows_list

    bin_rows_list[row][col] = '0'

    bin_rows_list = convert_filled_adjacent(row + 1,
                                            col,
                                            bin_rows_list)
    bin_rows_list = convert_filled_adjacent(row,
                                            col + 1,
                                            bin_rows_list)
    bin_rows_list = convert_filled_adjacent(row,
                                            col - 1,
                                            bin_rows_list)
    bin_rows_list = convert_filled_adjacent(row - 1,
                                            col,
                                            bin_rows_list)
    return bin_rows_list
    

def count_groups(bin_rows_list):
    num_of_groups = 0
    nrows = len(bin_rows_list)
    ncols = len(bin_rows_list[0])
    for row in range(nrows):
        for col in range(ncols):
            element = bin_rows_list[row][col]
            if element == '1':
                num_of_groups += 1
                bin_rows_list = convert_filled_adjacent(row,
                                                        col,
                                                        bin_rows_list)
    return num_of_groups


if __name__ == '__main__':
    input_string = 'nbysizxe'
    # input_string = 'flqrgnkx'
    input_strings = build_input_strings(input_string)
    hashed_rows = ['0x' + dt.hash(s) for s in input_strings]
    bin_rows = [bin(int(x, 16))[2:] for x in hashed_rows]
    suma = reduce(lambda i, bs: i + bs.count('1'), bin_rows, 0) 
    print('sum: ', suma)

    for index, row in enumerate(bin_rows):
        while len(bin_rows[index]) < 128:
            bin_rows[index] = '0' + bin_rows[index] 

    suma = reduce(lambda i, bs: i + bs.count('1'), bin_rows, 0) 
    print('sum: ', suma)

    bin_rows_list = [list(row) for row in bin_rows]
    number_of_groups = count_groups(bin_rows_list)
    print(number_of_groups)
