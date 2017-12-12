import pytest
import day_201712010 as ten

def test_basic_hash():
    lengths = [3, 4, 1, 5]
    sequence = list(range(5))
    position = 0
    skip_size = 0
    assert ten.basic_hash(sequence, lengths, position, skip_size)['sequence'] == [3, 4, 2, 1, 0]

    lengths = [0]
    sequence = list(range(5))
    position = 0
    skip_size = 0
    assert ten.basic_hash(sequence, lengths, position, skip_size)['sequence'] == [0, 1, 2, 3, 4]

    lengths = [7]
    sequence = list(range(5))
    position = 0
    skip_size = 0
    assert ten.basic_hash(sequence, lengths, position, skip_size)['sequence'] == [1, 0, 4, 3, 2]

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


# def test_convert_char_to_ASCII():
#     assert ten.convert_char_to_ASCII('0') == 48
#     assert ten.convert_char_to_ASCII('1') == 49
#     assert ten.convert_char_to_ASCII('2') == 50
#     assert ten.convert_char_to_ASCII('3') == 51
#     assert ten.convert_char_to_ASCII('4') == 52
#     assert ten.convert_char_to_ASCII('5') == 53
#     assert ten.convert_char_to_ASCII('6') == 54
#     assert ten.convert_char_to_ASCII('7') == 55
#     assert ten.convert_char_to_ASCII('8') == 56
#     assert ten.convert_char_to_ASCII('9') == 57
#     assert ten.convert_char_to_ASCII(',') == 44


def test_densify_hash():
    sparse_hash = list(range(256))
    assert ten.densify_hash(sparse_hash) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    sparse_hash = list(range(256))
    sparse_hash[0:16] = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    assert ten.densify_hash(sparse_hash) == [64, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_hex_representation():
    dense_hash = [16, 48, 16, 112, 16, 48, 16, 240, 16, 48, 16, 112, 16, 48, 1, 222]
    assert ten.hex_representation(dense_hash) == '10301070103010f010301070103001de'


def test_real_hashing():
    input_string = ''
    assert ten.real_hashing(input_string) == [38,171,116,63,70,137,168,29,198,55,160,15,34,95,58,7,188,189,238,141,30,31,124,241,20,1,244,203,234,73,236,211,122,197,94,227,142,57,72,239,54,81,154,217,10,13,186,161,6,17,128,105,106,69,44,51,248,23,136,173,52,39,40,5,254,195,64,187,192,37,230,153,56,177,84,147,96,249,252,121,166,143,62,169,90,99,196,155,132,159,162,229,76,117,164,127,150,21,88,27,242,67,114,115,226,191,190,53,2,65,206,205,24,251,14,75,74,247,80,11,50,181,46,101,100,179,48,131,32,97,102,201,170,93,104,103,182,125,12,43,220,113,158,167,68,47,66,33,112,135,194,185,218,219,8,245,130,253,204,243,202,109,92,209,156,133,250,107,4,183,60,215,172,231,240,83,98,193,82,139,210,91,146,85,184,163,140,145,178,35,232,151,214,213,200,199,18,221,212,9,152,123,78,3,228,25,26,225,0,61,138,255,222,233,110,129,208,207,176,235,108,77,148,19,180,79,28,149,224,237,86,157,216,111,22,89,16,41,144,71,134,59,246,165,174,223,118,119,36,175,126,87,120,45,42,49]


def test_hash():
    input_string = 'AoC 2017'
    assert hash(input_string) == '33efeb34ea91902bb2f59c9920caa6cd'

    input_string = '1,2,3'
    assert hash(input_string) == '3efbe78a8d82f29979031a4aa0b16a9d'
