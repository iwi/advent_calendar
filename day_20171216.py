#!/usr/bin/env python3
"""
Solution to problem 16
"""

import csv

# Part one
def identify_type(move):
    if move[0] == 's':
        return 'spin'
    if move[0] == 'x':
        return 'exchange'
    if move[0] == 'p':
        return 'partner'
    return 'UNKNOWN MOVE!!'


def spin(group, size):
    part1 = group[:-size]
    part2 = group[-size:]
    return part2 + part1


def get_positions(x_move):
    positions = x_move.split('/')
    return [int(pos) for pos in positions]


def exchange(group, positions):
    p0 = positions[0]
    p1 = positions[1]
    group[p0], group[p1] = group[p1], group[p0]
    return group


def get_partner_positions(group, p_move):
    to_x = p_move.split('/')
    positions = []
    for index, element in enumerate(group):
        if element == to_x[0]:
            positions.append(index)
            break

    for index, element in enumerate(group):
        if element == to_x[1]:
            positions.append(index)
            break

    return positions


def dance(group, moves):
    for move in moves:
        type = identify_type(move)
        if type == 'spin':
            size = int(move[1:])
            group = spin(group, size)
        if type == 'exchange':
            positions = get_positions(move[1:])
            group = exchange(group, positions)
        if type == 'partner':
            positions = get_partner_positions(group, move[1:])
            group = exchange(group, positions)

    return group


if __name__ == '__main__':
    moves = []
    with open('data/input_data_20171216.csv', 'r') as csvfile:
    # with open('data/test_16.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        moves = sum(list(data), [])
    
    group = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    print(group)

    print(dance(group, moves))

