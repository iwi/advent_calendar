#!/usr/bin/env python3
"""
Solution to problem 11
"""

import csv
import collections as c

# Part one
def reduce_pairs(dirs):
    n = dirs['n']
    s = dirs['s']
    ne = dirs['ne']
    nw = dirs['nw']
    se = dirs['se']
    sw = dirs['sw']

    reduced_dirs = {}
    reduced_dirs['n'] = n - min(n, s)
    reduced_dirs['s'] = s - min(n, s)
    reduced_dirs['nw'] = nw - min(nw, se)
    reduced_dirs['se'] = se - min(nw, se)
    reduced_dirs['ne'] = ne - min(ne, sw)
    reduced_dirs['sw'] = sw - min(ne, sw)

    return reduced_dirs


def reduce_triplets(dirs):
    n = dirs['n']
    s = dirs['s']
    ne = dirs['ne']
    nw = dirs['nw']
    se = dirs['se']
    sw = dirs['sw']

    reduced_dirs = {}
    reduced_dirs['n'] = n - min(n, sw, se)
    reduced_dirs['sw'] = sw - min(n, sw, se)
    reduced_dirs['se'] = se - min(n, sw, se)
    reduced_dirs['s'] = s - min(s, nw, ne)
    reduced_dirs['nw'] = nw - min(s, nw, ne)
    reduced_dirs['ne'] = ne - min(s, nw, ne)

    return reduced_dirs


def compress(dirs):
    n = dirs['n']
    s = dirs['s']
    ne = dirs['ne']
    nw = dirs['nw']
    se = dirs['se']
    sw = dirs['sw']
    

    compressed_dirs = {}

    if n > se:
        se = 0
    else:
        n = 0

    if nw > s:
        s = 0
    else:
        nw = 0

    if sw > se:
        se = 0
    else:
        sw = 0

    if s > ne:
        ne = 0
    else:
        s = 0

    if ne > nw:
        nw = 0
    else:
        ne = 0

    if n > sw:
        sw = 0
    else:
        n = 0

    compressed_dirs['n']  = n 
    compressed_dirs['s']  = s 
    compressed_dirs['ne'] = ne
    compressed_dirs['nw'] = nw
    compressed_dirs['se'] = se
    compressed_dirs['sw'] = sw

    return compressed_dirs


if __name__ == '__main__':
    directions = []
    with open('data/input_data_20171211.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        directions = sum(list(data), [])
        dir_count = c.Counter(directions)
        print(dir_count)
        reduced_count = reduce_pairs(dir_count)
        print(reduced_count)
        reduced_count = reduce_triplets(reduced_count)
        print(reduced_count)
        compressed_count = compress(reduced_count)
        print(compressed_count)
        print(sum(compressed_count.values()))


        
        
