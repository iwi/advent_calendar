#!/usr/bin/env python3
"""
AoC solution day seventeen
"""

def add_lock(spinlock, steps, position):
    size = len(spinlock)
    position = int((position + steps) % size) + 1
    spinlock.insert(position, size)
    return spinlock, position


def find_value_after(number, spinlock):
    for index, element in enumerate(spinlock):
        if element == number:
            return index + 1


##### solution seen on Reddit
# https://www.reddit.com/r/adventofcode/comments/7kdbni/2017_day_17_python_3_using_numba_for_a_10x_speed/

def next0(step):
    pos = 0
    final = 0
    for i in range(1, 50000001):
        pos = (pos + step) % i + 1
        if pos == 1:
            final = i
    return final


if __name__ == '__main__':
    spinlock = [0]
    steps = 363
    position = 0
    size = 2018
    for iter in range(size):
        spinlock, position = add_lock(spinlock, steps, position)
        if (iter % 100000) == 0:
            print(iter)
        
    index_after_2017 = find_value_after(2017, spinlock)
    print("index {}".format(index_after_2017))
    print('value after 2017 {}'.format(spinlock[index_after_2017]))

    # index_after_0 = find_value_after(0, spinlock)
    # print("index {}".format(index_after_0))
    # print('value after 0 {}'.format(spinlock[index_after_0]))

    print(print('Value after 0 in completed buffer is', next0(steps)))
