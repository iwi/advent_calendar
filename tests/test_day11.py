import pytest
import day_20171211 as e

def test_reduce_pairs():
    seq = {'n': 5, 's': 5, 'ne': 6, 'nw': 8, 'se': 8, 'sw': 6} 
    assert e.reduce_pairs(seq) == {'n': 0, 's': 0, 'ne': 0, 'nw': 0, 'se': 0, 'sw': 0} 


    seq = {'n': 1653, 's': 1345, 'ne': 1456, 'nw': 1294, 'se': 1393, 'sw': 1082} 
    assert e.reduce_pairs(seq) == {'n': 308, 's': 0, 'ne': 374, 'nw': 0, 'se': 99, 'sw': 0} 
    

def test_reduce_triplets():
    seq = {'n': 9, 's': 12, 'ne': 9, 'nw': 8, 'se': 8, 'sw': 6} 
    assert e.reduce_triplets(seq) == {'n': 3, 's': 4, 'ne': 1, 'nw': 0, 'se': 2, 'sw': 0} 

# def test_compress():
#     seq = {'n': 9, 's': 12, 'ne': 9, 'nw': 8, 'se': 8, 'sw': 6} 
#     assert e.compress(seq) == {'n': 3, 's': 4, 'ne': 1, 'nw': 0, 'se': 2, 'sw': 0} 
    

    
