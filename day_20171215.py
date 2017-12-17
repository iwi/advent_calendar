#!/usr/bin/env python3
"""
AoC solution day 15
"""


def expand_bin(bin_num): 
    expanded = bin_num[2:]
    while len(expanded) < 128:
        expanded = '0' + expanded
    return expanded


def calc_next_val(prev, factor, div):
    return (prev * factor) % div


def get_next_pair(prev_a, prev_b, a_factor, b_factor, div, mult_a, mult_b):
    next_a = calc_next_val(prev_a, a_factor, div)
    while (next_a % mult_a) != 0:
        next_a = calc_next_val(next_a, a_factor, div)

    next_b = calc_next_val(prev_b, b_factor, div)
    while (next_b % mult_b) != 0:
        next_b = calc_next_val(next_b, b_factor, div)
    return next_a, next_b


def compare_pair_16(val_a, val_b):
    last_16_a = expand_bin(bin(val_a))[-16:]
    last_16_b = expand_bin(bin(val_b))[-16:]
    return last_16_a == last_16_b


def count_matches(origin_a, origin_b, a_factor, b_factor, div, number_of_pairs):
    counter = 0
    mult_a = 4
    mult_b = 8
    prev_a = origin_a
    prev_b = origin_b
    for rep in range(number_of_pairs):
        print('pair number {}'.format(rep))
        prev_a, prev_b = get_next_pair(prev_a,
                                       prev_b,
                                       a_factor,
                                       b_factor,
                                       div,
                                       mult_a,
                                       mult_b)
        equal_16 = compare_pair_16(prev_a, prev_b)
        if equal_16:
            counter += 1
    return counter


if __name__ == '__main__':
    # origin_a = 65
    origin_a = 618
    # origin_b = 8921
    origin_b = 814
    a_factor = 16807
    b_factor = 48271
    div = 2147483647
    number_of_pairs = 5000000

    matches = count_matches(origin_a,
                            origin_b,
                            a_factor,
                            b_factor,
                            div,
                            number_of_pairs)
    print("The number of matches is {}".format(matches))
