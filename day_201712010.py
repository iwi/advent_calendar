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
    print('sequence ', sequence)
    start = int(position)
    print('start ', start)
    if length <= len(sequence):
        end = int((position + length) % len(sequence)) - 1
    else:
        if start == 0:
            end = len(sequence)
        else:
            end = start - 1
    print('end ', end)
    subsequence = get_subsequence(start, end, sequence)
    print('subsequence', subsequence)
    transformed_subsequence = list(reversed(subsequence))
    print('transformed subseq ', transformed_subsequence)
    transformed_sequence = substitute_subsequence(transformed_subsequence, sequence, start, end, length) 
    print('transformed sequence ', transformed_sequence)
    transformed_status = status.copy()
    transformed_status['position'] = int((position + length + skip_size) % len(sequence))
    if length != 0:
        transformed_status['sequence'] = transformed_sequence
    print(status)
    transformed_status['skip_size'] += 1
    print(status)
    return transformed_status


def hash(sequence, lengths, position, skip_size):
    status = {
        'position': position,
        'skip_size': skip_size,
        'sequence': sequence}
    print(status)

    for skip_size, length in enumerate(lengths):
        status = apply_length(length, status)
        print(status)
    
    return status


def checksum(hash):
    return hash[0] * hash[1]


# Part 2

def convert_char_to_ASCII(char):
    dictionary = {
        '0': 48,
        '1': 49,
        '2': 50,
        '3': 51,
        '4': 52,
        '5': 53,
        '6': 54,
        '7': 55,
        '8': 56,
        '9': 57,
        ',': 44 
    }
    return dictionary[char]




if __name__ == '__main__':
    lengths = []
    with open('data/input_data_201712010.csv', 'r') as csvfile:
    # with open('data/test_10_2.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for element in data:
            lengths.append(element)
        lengths = sum(lengths, [])
        ascii_list = []
        for element in lengths:
            ascii_lengths = [ord(str(item)) for item in str(int(element))]
            ascii_list.append(ascii_lengths)
        ll = []
        for x in ascii_list:
            ll.append(44)
            for y in x:
                ll.append(y)

        ll.pop(0)
        for element in [17, 31, 73, 47, 23]:
            ll.append(element)


        sequence = list(range(256))
        hashed_sequence = hash(sequence, lengths, 0, 0)['sequence']
        print('Checksum: ', checksum(hashed_sequence))
