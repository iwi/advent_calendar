#!/usr/bin/env python3
"""
AoC solution day 21
"""

import re
import numpy as np


def parse_line(l):
    parts = "([\.|#]+)"
    captures = re.findall(parts, l)
    rule = []
    for c in captures:
        p = list(c)
        part = []
        for item in p:
            if item == '.':
                part.append(0)
            elif item == '#':
                part.append(1)
        rule.append(part)
    if len(rule) == 5:
        return [[rule[0], rule[1]], [rule[2], rule[3], rule[4]]]
    elif len(rule) == 7:
        return [[rule[0], rule[1], rule[2]], [rule[3], rule[4], rule[5], rule[6]]]


def get_piece(n, m, side, pattern):
    v = int(n * side)
    h = int(m * side)
    rg_h = range(h, h + side)
    rg_v = range(v, v + side)
    piece = [[pattern[row][col] for col in rg_h] for row in rg_v]
    return piece


def splitter(size, pieces_side, pattern):
    num_of_pieces_side = int(size / pieces_side)
    pieces = [[get_piece(n, m, pieces_side, pattern) for m in range(num_of_pieces_side)] for n in range(num_of_pieces_side)]
    return pieces


def rotate(piece, times):
    if np.shape(piece)[0] == 2:
        return rotate2(piece, times)
    elif np.shape(piece)[0] == 3:
        return rotate3(piece, times)


def rotate2(piece, times):
    if times == 0:
        return piece
    else:
        times -= 1
        piece = [[piece[1][0], piece[0][0]],
                 [piece[1][1], piece[0][1]]]
        return rotate(piece, times)


def rotate3(piece, times):
    if times == 0:
        return piece
    else:
        times -= 1
        piece = [[piece[2][0], piece[1][0], piece[0][0]],
                 [piece[2][1], piece[1][1], piece[0][1]],
                 [piece[2][2], piece[1][2], piece[0][2]]]
        return rotate(piece, times)


def get_transforms(piece):
    if np.shape(piece)[0] == 2:
        rot_90 = rotate(piece, 1)
        rot_180 = rotate(piece, 2)
        rot_270 = rotate(piece, 3)
        flip_v = [piece[1], piece[0]] 
        fv_rot_90 = rotate(flip_v, 1)
        fv_rot_180 = rotate(flip_v, 2)
        fv_rot_270 = rotate(flip_v, 3)
        flip_h = [[piece[0][1], piece[0][0]], [piece[1][1], piece[1][0]]]
        fh_rot_90 = rotate(flip_h, 1)
        fh_rot_180 = rotate(flip_h, 2)
        fh_rot_270 = rotate(flip_h, 3)

    elif np.shape(piece)[0] == 3:
        rot_90 = rotate(piece, 1)
        rot_180 = rotate(piece, 2)
        rot_270 = rotate(piece, 3)
        flip_v = [piece[2], piece[1], piece[0]] 
        fv_rot_90 = rotate(flip_v, 1)
        fv_rot_180 = rotate(flip_v, 2)
        fv_rot_270 = rotate(flip_v, 3)
        flip_h = [[piece[0][2], piece[0][1], piece[0][0]],
                  [piece[1][2], piece[1][1], piece[1][0]],
                  [piece[2][2], piece[2][1], piece[2][0]]]
        fh_rot_90 = rotate(flip_h, 1)
        fh_rot_180 = rotate(flip_h, 2)
        fh_rot_270 = rotate(flip_h, 3)

    return [piece, flip_v, flip_h, rot_90, rot_180, rot_270, fv_rot_90,
            fv_rot_180, fv_rot_270, fh_rot_90, fh_rot_180, fh_rot_270]


def find_canonical(piece, rules):
    size = np.shape(piece)[0]
    transforms = get_transforms(piece)
    for transform in transforms:
        for index, rule in enumerate(rules):
            if transform == rule[0]:
                return transform

        
def split_pattern(pattern):
    size = np.shape(pattern)[0]
    if (size % 2) == 0:
        pieces = splitter(size, 2, pattern)
    elif (size % 3) == 0:
        pieces = splitter(size, 3, pattern)
    return pieces


def transform(canonical, rules):
    for index, rule in enumerate(rules):
        if rule[0] == canonical:
            return rules[index][1]


def convert_piece(piece, rules):
    canonical = find_canonical(piece, rules)
    new_piece = transform(canonical, rules)
    return new_piece


def convert_all(pieces, rules):
    size = np.shape(pieces)[0]
    converted = [[convert_piece(pieces[col][row], rules) for col in range(size)] for row in range(size)]
    return converted


def attach(trans):
    size = np.shape(trans)[0]
    elements = np.shape(trans)[2]
    attached = []
    for row in range(size):
         for elem in range(elements):
            line = []
            for col in range(size):
                line += trans[row][col][elem]
            attached.append(line)    
    return attached


def iterate(pattern, rules):
    pieces = split_pattern(pattern)
    trans_pieces = convert_all(pieces, rules)
    new_pattern = attach(trans_pieces)
    return new_pattern


def expand_image(pattern, rules, iterations):
    for i in range(iterations):
        pattern = iterate(pattern, rules)
    return pattern


if __name__ == '__main__':
    lines = []
    with open('data/input_data_20171221.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))

    rules = [parse_line(line) for line in lines]
    origin = [[0, 1, 0],
              [0, 0, 1],
              [1, 1, 1]]
    
    # [print(rule[0]) for rule in rules]

    pattern = expand_image(origin, rules, 4)

    print('pattern:')
    print(pattern)
    print(sum([sum(e) for e in pattern]))



