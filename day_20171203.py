#!/usr/bin/env python3
"""
AoC solution day three 
2017-12-03
"""
def get_minimum_larger_square(n):
    m = 0
    while n > (2 * m + 1)**2:
        m += 1

    return m


def calc_manhattan_distance_in_spiral_from(n):
    if n = 1:
        return 1
    m = minimum_larger_square_base = get_minimum_larger_square(n)
    k = n - (2 * m - 1)**2
    reminder = k % (2 * m)
    if reminder >= m:
        return reminder
    else:
        return 2 * m - reminder


if __name__ == '__main__':
    steps = calc_manhattan_distance_in_spiral_from(368078)
    print('solution: ', steps)
