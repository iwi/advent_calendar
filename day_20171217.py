#!/usr/bin/env python3
"""
AoC solution day seventeen
"""
import re
import statistics as st

def add_lock(spinlock, steps, position):
    size = len(spinlock)
    position = int((position + steps) % size) + 1
    spinlock.insert(position, size)
    return spinlock, position


def find_value_after(number, spinlock):
    for index, element in enumerate(spinlock):
        if element == number:
            return index + 1


if __name__ == '__main__':
    spinlock = [0]
    steps = 363
    position = 0
    size = 100
    for iter in range(size):
        spinlock, position = add_lock(spinlock, steps, position)

    print(spinlock)
        
    index_after_2017 = find_value_after(2017, spinlock)
    print("index {}".format(index_after_2017))
    print('value after 2017 {}'.format(spinlock[index_after_2017]))

    index_after_0 = find_value_after(0, spinlock)
    print("index {}".format(index_after_0))
    print('value after 0 {}'.format(spinlock[index_after_0]))
