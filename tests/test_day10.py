import pytest
import day_201712010 as ten

def test_hash():
    lengths = [3, 4, 1, 5]
    sequence = list(range(5))
    assert ten.hash(sequence, lengths) == [3, 4, 2, 1, 0]


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
    assert ten.substitute_subsequence(subsequence, sequence, start, end) == [4, 3, 2, 1, 0]

    subsequence = [3, 2, 1]
    sequence = [0, 1, 2, 3, 4]
    start = 1
    end = 3
    assert ten.substitute_subsequence(subsequence, sequence, start, end) == [0, 3, 2, 1, 4]

    subsequence = [4, 2, 1, 0, 3]
    sequence = [4, 3, 0, 1, 2]
    start = 1
    end = 0
    assert ten.substitute_subsequence(subsequence, sequence, start, end) == [3, 4, 2, 1, 0]


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
    
def test_checksum():
    hashed_sequence = [4, 3, 0, 1, 2]
    assert ten.checksum(hashed_sequence) == 12
