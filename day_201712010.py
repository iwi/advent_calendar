#!/usr/bin/env python3
"""
Solution to problem 10
"""

import csv
from functools import reduce

# Part one
def get_subsequence(start, end, sequence):
    if end >= start:
        return sequence[start:end + 1]
    else:
        return sequence[start:] + sequence[:end + 1]


def substitute_subsequence(subsequence, sequence, start, end, length):
    if end >= start:
        if length <= len(sequence):
            sequence[start:end + 1] = subsequence
        else:
            start = start + int(length % len(sequence))
            end = start - 1
            sequence[start:] = subsequence[:len(sequence[start:])]
            sequence[:end + 1] = subsequence[len(sequence) - start:]
    else:
        sequence[start:] = subsequence[:len(sequence[start:])]
        sequence[:end + 1] = subsequence[len(sequence) - start:]

    return sequence


def apply_length(length, status):
    position = int(status['position'])
    skip_size = status['skip_size']
    sequence = status['sequence'].copy()
    # print('sequence ', sequence)
    start = int(position)
    # print('start ', start)
    if length <= len(sequence):
        end = int((position + length) % len(sequence)) - 1
    else:
        if start == 0:
            end = len(sequence)
        else:
            end = start - 1
    # print('end ', end)
    subsequence = get_subsequence(start, end, sequence)
    # print('subsequence', subsequence)
    transformed_subsequence = list(reversed(subsequence))
    # print('transformed subseq ', transformed_subsequence)
    transformed_sequence = substitute_subsequence(transformed_subsequence, sequence, start, end, length) 
    # print('transformed sequence ', transformed_sequence)
    transformed_status = status.copy()
    transformed_status['position'] = int((position + length + skip_size) % len(sequence))
    if length != 0:
        transformed_status['sequence'] = transformed_sequence
    # print(status)
    transformed_status['skip_size'] += 1
    # print(status)
    return transformed_status


def basic_hash(sequence, lengths, position, skip_size):
    status = {
        'position': position,
        'skip_size': skip_size,
        'sequence': sequence}
    for skip_size, length in enumerate(lengths):
        status = apply_length(length, status)
        # print(status)
    return status


def densify_hash(sparse_hash):
    slice_16 = []
    for i in range(0, 256, 16):
        slice_16.append(sparse_hash[i:i + 16])
    dense_hash = []
    for rg in slice_16:
        dense_hash.append(reduce(lambda x, y: x ^ y, rg))
    return dense_hash


def hex_representation(dense_hash):
    hexhash = ''
    for element in dense_hash:
        hexhash += my_hex(element)
    return hexhash


def checksum(hash):
    return hash[0] * hash[1]


# Part 2

# def convert_char_to_ASCII(char):
#     dictionary = {
#         '0': 48,
#         '1': 49,
#         '2': 50,
#         '3': 51,
#         '4': 52,
#         '5': 53,
#         '6': 54,
#         '7': 55,
#         '8': 56,
#         '9': 57,
#         ',': 44 
#     }
#     return dictionary[char]

def real_hashing(input_string):
    ll = []
    for ch in input_string:
        ll.append(ord(ch))
    ll = ll + [17, 31, 73, 47, 23]
    print(ll)
    lengths = ll[:]
    sequence = list(range(256))
    status = {
        'position': 0,
        'skip_size': 0,
        'sequence': sequence}
    for i in range(64):
        status = basic_hash(sequence, lengths, status['position'], status['skip_size'])

    return status['sequence']


def my_hex(num):
    mh = hex(num)[2:]
    if len(mh) < 2:
        return '0' + mh
    elif len(mh) == 2:
        return mh
   

def reverse(text, repeat):
    knot = list(range(256))
    pos = 0
    skip = 0
    for isntevenused in range(repeat):
        for i in text:
            temp = []
            for j in range(i):
                temp.append(knot[(pos+j) % 256])
            for j in range(i):
                knot[(pos+i-1-j) % 256] = temp[j]
            pos += skip + i
            skip += 1
    return knot

def hash(input):
    # sparse_hash = real_hashing(input_string)
    input_string = []
    for i in range(len(input)):
        input_string.append(ord(input[i]))
    input_string += [17, 31, 73, 47, 23]
    sparse_hash = reverse(input_string, 64)
    dense_hash = densify_hash(sparse_hash)
    print(dense_hash)
    hex_hash = hex_representation(dense_hash)
    return str(hex_hash)

if __name__ == '__main__':
    lengths = []
    with open('data/input_data_201712010.csv', 'r') as csvfile:
    # with open('data/test_10_2.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for element in data:
            lengths.append(element)
        lengths = sum(lengths, [])


        input_string = ''
        for element in lengths:
            input_string += ',' + str(int(element))
            input_string = input_string[1:]

        print('input string:', input_string)

        hex_hash = hash(input_string)
        print('hash: ', hex_hash)
        
        sequence = list(range(256))
        hashed_sequence = basic_hash(sequence, lengths, 0, 0)['sequence']
        print('Checksum: ', checksum(hashed_sequence))



####################################
# from
# https://www.reddit.com/r/adventofcode/comments/7irzg5/2017_day_10_solutions/
###################################
from time import time


def reverse(text, repeat):
    knot = list(range(256))
    pos = 0
    skip = 0
    for isntevenused in range(repeat):
        for i in text:
            temp = []
            for j in range(i):
                temp.append(knot[(pos+j) % 256])
            for j in range(i):
                knot[(pos+i-1-j) % 256] = temp[j]
            pos += skip + i
            skip += 1
    return knot


def dense(knot):
    dense = [0]*16
    for i in range(16):
        dense[i] = knot[16*i]
        for m in range(1, 16):
            dense[i] ^= knot[16*i+m]
    return dense


def kh(dense):
    knothash = ''
    for i in dense:
        if len(hex(i)[2:]) == 2:
            knothash += hex(i)[2:]
        else:
            knothash += '0' + hex(i)[2:]
    return knothash


start = time()

inp = '63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24'
text = [63,144,180,149,1,255,167,84,125,65,188,0,2,254,229,24]
inp = '31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33'
text = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]
text2 = []

for i in range(len(inp)):
    text2.append(ord(inp[i]))
text2 += [17, 31, 73, 47, 23]

knot = reverse(text, 1)
sparce = reverse(text2, 64)

dense = dense(sparce)
knothash = kh(dense)

print('Part One: ' + str(knot[0]*knot[1]))
print('Part Two: ' + knothash)
print('Completed in ' + str(time() - start) + ' seconds.')

######################

