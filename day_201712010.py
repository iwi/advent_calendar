#!/usr/bin/env python3
"""
Solution to problem 10
"""

import csv

# Part one
def get_subsequence(start, end, sequence):
    if end >= start:
        return sequence[start:end + 1]
    else:
        return sequence[start:] + sequence[:end + 1]


def substitute_subsequence(subsequence, sequence, start, end):
    if end >= start:
        sequence[start:end + 1] = subsequence
    else:
        sequence[start:] = subsequence[:len(sequence[start:])]
        sequence[:end + 1] = subsequence[len(sequence) - start:]

    return sequence


def apply_length(length, status):
    position = int(status['position'])
    skip_size = status['skip_size']
    sequence = status['sequence']
    start = int(position)
    end = int((position + length) % len(sequence)) - 1
    subsequence = get_subsequence(start, end, sequence)
    transformed_subsequence = list(reversed(subsequence))
    transformed_sequence = substitute_subsequence(transformed_subsequence, sequence, start, end)
    transformed_status = status.copy()
    transformed_status['position'] = int((position + length + skip_size) % len(sequence))
    transformed_status['sequence'] = transformed_sequence
    transformed_status['skip_size'] += 1
    return transformed_status


def hash(sequence, lengths):
    status = {
        'position': 0,
        'skip_size': 0,
        'sequence': sequence}
    print(status)

    for skip_size, length in enumerate(lengths):
        status = apply_length(length, status)
        print(status)
    
    return status['sequence']


def checksum(hash):
    return hash[0] * hash[1]


if __name__ == '__main__':
    lengths = []
    with open('data/input_data_201712010.csv', 'r') as csvfile:
    # with open('data/test_10.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for element in data:
            lengths.append(element)
        lengths = sum(lengths, [])

        sequence = list(range(256))
        hashed_sequence = hash(sequence, lengths)
        print('Checksum: ', checksum(hashed_sequence))
