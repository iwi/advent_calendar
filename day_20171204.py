#!/usr/bin/env python3
"""
AoC solution day four 
2017-12-04
"""

def is_valid(passphrase):
    """
    validate passphrases with no repeats
    """
    list_of_words = passphrase.split()
    valid = True
    for word in list_of_words:
        valid_word = list_of_words.count(word) == 1
        valid = valid & valid_word
    return valid 

if __name__ == '__main__':
    tt = []
    with open('data/input_data_20171204.txt', 'r') as f:
           for line in f:
               tt.append(line.rstrip())

    total = sum(list(map(is_valid, tt)))
    print('valid passwords: ', total)

    assert is_valid('aa aa bb') is False
    assert is_valid('a b c d') is True

