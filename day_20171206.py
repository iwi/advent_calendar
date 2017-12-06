#!/usr/bin/env python3
"""
Solution to problem 6
"""

import csv

# Part one
def is_known(memory_distribution, known_distributions):
    for distribution in known_distributions:
        if distribution == memory_distribution:
            return True
    return False


def redistribute(memory_distribution):
    max_index = int(memory_distribution.index(max(memory_distribution)))
    max_value = memory_distribution[max_index]
    memory_distribution[max_index] = 0
    length = len(memory_distribution)
    min_extra = int(max_value / length)
    number_of_specials = int(max_value % length)
    # all get the extra minimum
    memory_distribution = list(map(lambda x: x + min_extra, memory_distribution))

    if number_of_specials == length - 1:
        memory_distribution = list(map(lambda x: x + 1, memory_distribution))
        memory_distribution[max_index] = min_extra
    elif (number_of_specials < length - 1) & (number_of_specials <= length - max_index - 1):
        for index in range(max_index + 1, max_index + number_of_specials + 1):
            memory_distribution[index] += 1
    elif (number_of_specials < length - 1) & (number_of_specials > length - max_index - 1):
        for index in range(max_index + 1, length):
            memory_distribution[index] += 1
        for index in range(0, number_of_specials - (length - max_index - 1)):
            memory_distribution[index] += 1

    return(memory_distribution)


def count_redistributions(memory_bank):
    known_distributions = []
    known_distributions.append(list(memory_bank))
    print(known_distributions)
    memory_distribution = list(redistribute(memory_bank))
    counter = 1

    while not is_known(memory_distribution, known_distributions):
        known_distributions.append(list(memory_distribution))
        print(sum(memory_distribution))
        memory_distribution = list(redistribute(memory_distribution))
        counter += 1
        print('counter:', counter, '   is_known:', is_known(memory_distribution, known_distributions))

    return counter


if __name__ == '__main__':
    memory_banks = []
    with open('data/input_data_20171206.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for element in data:
            memory_banks.append(element)

        memory_banks = sum(memory_banks, [])
        print(count_redistributions(memory_banks))
        test_memory_banks = [0, 2, 7, 0]
        print(count_redistributions(test_memory_banks))
