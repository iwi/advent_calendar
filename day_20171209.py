#!/usr/bin/env python3
"""
AoC solution day nine 
2017-12-09
"""

# Part 1

def apply_escaper(status):
    if status['open_escaper'] is 'on':
        status['open_escaper'] = 'off'
    else:
        status['open_escaper'] = 'on'
    return status

def open_rubbish(status):
    if status['open_escaper'] is 'on':
        status['open_escaper'] = 'off'
        return status

    if status['open_rubbish'] is 'off':
        status['open_rubbish'] = 'on'
    return status

def close_rubbish(status):
    if status['open_escaper'] is 'on':
        status['open_escaper'] = 'off'
        return status
    if status['open_rubbish'] is 'on':
        status['open_rubbish'] = 'off'
    return status


def open_group(status):
    if status['open_escaper'] is 'on':
        status['open_escaper'] = 'off'
        return status
    if status['open_rubbish'] is 'off':
        status['open_curlies'] += 1
    return status


def close_group(status):
    if status['open_escaper'] is 'on':
        status['open_escaper'] = 'off'
        return status
    if status['open_rubbish'] is 'off':
        if status['open_curlies'] > 0:
            status['group_counter'] += status['open_curlies']
            status['open_curlies'] -= 1
    return status
    

def react(char, status):
    return {
        '!': lambda status: apply_escaper(status),
        '<': lambda status: open_rubbish(status),
        '>': lambda status: close_rubbish(status),
        '{': lambda status: open_group(status),
        '}': lambda status: close_group(status)}[char](status)


def update(status, char):
    meaningful_chars = ['!', '<', '>', '{', '}']
    if char not in meaningful_chars:
        if status['open_escaper'] is 'on':
            status['open_escaper'] = 'off'
        return status
    status = react(char, status)
    return status


def count_groups(stream):
    status = {
        'group_counter': 0,
        'open_curlies': 0,
        'open_rubbish': 'off',
        'open_escaper': 'off'}

    for char in stream:
        status = update(status, char)
        print(char)
        print(status)

    return status['group_counter']


if __name__ == '__main__':
    stream = " "
    with open('data/input_data_20171209.txt', 'r') as f:
    # with open('data/test_9.txt', 'r') as f:
        stream = f.read().rstrip()

    stream = list(str(stream))
    groups = count_groups(stream)
    print(groups)
