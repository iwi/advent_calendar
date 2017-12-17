import pytest
import day_20171215 as f

def test_calc_next_val():
    prev = 65
    factor = 16807
    div = 2147483647
    next = 1092455
    assert f.calc_next_val(prev, factor, div) == next 


def test_expand_bin():
    bin_num = bin(1234)
    assert len(f.expand_bin(bin_num)) == 128

    bin_num = bin(1234)
    expanded = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010011010010'
    assert f.expand_bin(bin_num) == expanded


def test_compare_pair():
    element_a = 1092455
    element_b = 430625591
    assert f.compare_pair_16(element_a, element_b) is False

    element_a = 245556042
    element_b = 1431495498
    assert f.compare_pair_16(element_a, element_b) is True

def test_get_next_pair():
    prev_a = 1092455
    prev_b = 430625591
    a_factor = 16807
    b_factor = 48271
    div = 2147483647
    next_a = 1181022009
    next_b = 1233683848
    assert f.get_next_pair(prev_a,
                           prev_b,
                           a_factor,
                           b_factor,
                           div) == (next_a, next_b)
