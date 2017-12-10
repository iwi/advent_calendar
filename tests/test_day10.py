import pytest
import day_201712010 as ten

def test_hash():
    lengths = [3, 4, 1, 5]
    sequence = list(range(5))
    position = 0
    skip_size = 0
    assert ten.hash(sequence, lengths, position, skip_size)['sequence'] == [3, 4, 2, 1, 0]

    lengths = [0]
    sequence = list(range(5))
    position = 0
    skip_size = 0
    assert ten.hash(sequence, lengths, position, skip_size)['sequence'] == [0, 1, 2, 3, 4]

    lengths = [7]
    sequence = list(range(5))
    position = 0
    skip_size = 0
    assert ten.hash(sequence, lengths, position, skip_size)['sequence'] == [1, 0, 4, 3, 2]

def test_get_subsequence():
    sequence = [0, 1, 2, 3, 4]
    start = 1
    end = 3
    assert ten.get_subsequence(start, end, sequence) == [1, 2, 3]

    start = 3
    end = 1
    assert ten.get_subsequence(start, end, sequence) == [3, 4, 0, 1]

    sequence = [0, 1, 2, 3, 4]
    start = 1
    end = 2
    assert ten.get_subsequence(start, end, sequence) == [1, 2]


def test_substitute_sequence():
    subsequence = [1, 0, 4, 3]
    sequence = [0, 1, 2, 3, 4]
    start = 3
    end = 1
    length = 4
    assert ten.substitute_subsequence(subsequence, sequence, start, end, length) == [4, 3, 2, 1, 0]

    subsequence = [3, 2, 1]
    sequence = [0, 1, 2, 3, 4]
    start = 1
    end = 3
    length = 3
    assert ten.substitute_subsequence(subsequence, sequence, start, end, length) == [0, 3, 2, 1, 4]

    subsequence = [4, 2, 1, 0, 3]
    sequence = [4, 3, 0, 1, 2]
    start = 1
    end = 0
    length = 5
    assert ten.substitute_subsequence(subsequence, sequence, start, end, length) == [3, 4, 2, 1, 0]


def test_apply_length():
    length = 3
    sequence = [0, 1, 2, 3, 4]
    status = {
            'position': 0,
            'skip_size': 0,
            'sequence': sequence}
    transformed_status = {
            'position': 3,
            'skip_size': 1,
            'sequence': [2, 1, 0, 3, 4]}
    assert ten.apply_length(length, status) == transformed_status

    length = 4
    sequence = [2, 1, 0, 3, 4]
    status = {
            'position': 3,
            'skip_size': 1,
            'sequence': sequence}
    transformed_status = {
            'position': 3,
            'skip_size': 2,
            'sequence': [4, 3, 0, 1, 2]}
    assert ten.apply_length(length, status) == transformed_status
        
    length = 5
    sequence = [4, 3, 0, 1, 2]
    status = {
            'position': 1,
            'skip_size': 3,
            'sequence': sequence}
    transformed_status = {
            'position': 4,
            'skip_size': 4,
            'sequence': [3, 4, 2, 1, 0]}
    assert ten.apply_length(length, status) == transformed_status

    length = 0
    sequence = [0, 1, 2, 3, 4]
    status = {
            'position': 0,
            'skip_size': 0,
            'sequence': sequence}
    transformed_status = {
            'position': 0,
            'skip_size': 1,
            'sequence': sequence}
    assert ten.apply_length(length, status) == transformed_status


def test_checksum():
    hashed_sequence = [4, 3, 0, 1, 2]
    assert ten.checksum(hashed_sequence) == 12


def test_convert_char_to_ASCII():
    assert ten.convert_char_to_ASCII('0') == 48
    assert ten.convert_char_to_ASCII('1') == 49
    assert ten.convert_char_to_ASCII('2') == 50
    assert ten.convert_char_to_ASCII('3') == 51
    assert ten.convert_char_to_ASCII('4') == 52
    assert ten.convert_char_to_ASCII('5') == 53
    assert ten.convert_char_to_ASCII('6') == 54
    assert ten.convert_char_to_ASCII('7') == 55
    assert ten.convert_char_to_ASCII('8') == 56
    assert ten.convert_char_to_ASCII('9') == 57
    assert ten.convert_char_to_ASCII(',') == 44
