#!/usr/bin/env python3
"""
AoC solution day three 
2017-12-03
"""

from functools import reduce


# Part one

def get_minimum_larger_square(n):
    m = 0
    while n > (2 * m + 1)**2:
        m += 1

    return m


def calc_manhattan_distance_in_spiral_from(n):
    if n == 1:
        return 1
    m = minimum_larger_square_base = get_minimum_larger_square(n)
    k = n - (2 * m - 1)**2
    reminder = k % (2 * m)
    if reminder >= m:
        return reminder
    else:
        return 2 * m - reminder


# Part two
def goes_up(index):
    m = get_minimum_larger_square(index)
    k = index - (2 * m - 1)**2
    return k < 8 * m / 4


def goes_left(index):
    m = get_minimum_larger_square(index)
    k = index - (2 * m - 1)**2
    return (k < 8 * m / 2) & (k > 8 * m / 4)


def goes_down(index):
    m = get_minimum_larger_square(index)
    k = index - (2 * m - 1)**2
    return (k < 8 * m * 3 / 4) & (k > 8 * m / 2)


def goes_right(index):  # superfluous
    m = get_minimum_larger_square(index)
    k = index - (2 * m - 1)**2
    return (k < 8 * m) & (k > 8 * m * 3 / 4)


def is_corner(index):
    m = get_minimum_larger_square(index)
    k = index - (2 * m - 1)**2
    return k % (2 * m) == 0


def is_pre_corner(index):
    return is_corner(index + 1)


def is_post_corner(index):
    return is_corner(index - 1)


def get_adjacent(index):
    if index == 1:
        return [1]
    if index == 2:
        return [1]

    m = get_minimum_larger_square(index)
    k = index - (2 * m - 1)**2
    indices = []
    # Always append previous elment
    indices.append(index - 1)

    # First ring particularities
    if m == 1:
        indices.append(1)
        if k == 8:
            indices.append(2)
            return indices
        if is_corner(index):
            return indices
        if is_post_corner(index):
            indices.append(index - 2)
            if k == 8 * m - 1:
                indices.append((2 * m - 1)**2 + 1)
            return indices
        
    # Case where it's the first element of a new ring    
    if k == 1:
        indices.append((2 * m - 3)**2 + 1)
        return indices

    if k == 2:
        indices.append(index - 2)
        indices.append((2 * m - 3)**2 + 1)
        indices.append((2 * m - 3)**2 + 2)
        return indices

    if k == (8 * m):
        indices.append((2 * m - 1)**2 + 1)
        indices.append((2 * m - 1)**2)
        return indices

    if is_corner(index):
        indices.append(int(k - k / m + (2 * m - 3)**2))
        return indices

    if is_pre_corner(index):
        indices.append(int(k - k / m + (2 * m - 3)**2))
        indices.append(indices[1] + 1)
        if k == 8 * m - 1:
            indices.append((2 * m - 1)**2 + 1)
        return indices

    if is_post_corner(index):
        indices.append(int(k - k / m + (2 * m - 3)**2))
        indices.append(indices[1] + 1)
        indices.append(index - 2)
        return indices

    # else is middle
    if goes_up(index):
        indices.append(k - 1 + (2 * m - 3)**2)
    if goes_left(index):
        indices.append(k - 3 + (2 * m - 3)**2)
    if goes_down(index):
        indices.append(k - 5 + (2 * m - 3)**2)
    if goes_right(index):
        indices.append(k - 7 + (2 * m - 3)**2)

    indices.append(indices[1] + 1)
    indices.append(indices[1] - 1)
    return indices

def get_spiral_val(index, spiral):
    try:
        value = spiral[index]
    except:
        value = get_element_value(index, spiral)

    return value


def get_element_value(index, spiral):
    if index == 0:
        return(1)

    adjacent = get_adjacent(index + 1)
    adjacent_corrected = [x - 1 for x in adjacent]
    values = list(map(lambda x: get_spiral_val(x, spiral), adjacent_corrected))
    value = reduce(lambda x, y: x + y, values)
    return value


def build_spiral_up_to_val(value):
    spiral = [1]
    index = 0 

    while spiral[index] < value:
        index += 1
        spiral.append(get_element_value(index, spiral))

    return index, spiral


    

if __name__ == '__main__':
    steps = calc_manhattan_distance_in_spiral_from(368078)
    print('solution: ', steps)

    index, spiral = build_spiral_up_to_val(368078)
    # spiral = get_spiral_up_to_val(368078)
    print(index)
    print(spiral)
    print(max(spiral))
