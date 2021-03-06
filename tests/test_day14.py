import pytest
import day_20171214 as f

def test_convert_filled_adjacent():
    bin_list = [['0', '1', '0', '1'],
                ['1', '0', '0', '1']]
    conv_bin_list = [['0', '1', '0', '1'],
                     ['1', '0', '0', '1']]
    row = 0
    col = 0
    assert f.convert_filled_adjacent(row,
                                     col,
                                     bin_list) == conv_bin_list

    bin_list = [['1', '1', '0', '1'],
                ['1', '0', '0', '1']]
    conv_bin_list = [['0', '0', '0', '1'],
                     ['0', '0', '0', '1']] 
    row = 0
    col = 0
    assert f.convert_filled_adjacent(row,
                                     col,
                                     bin_list) == conv_bin_list

    bin_list = [['0', '1', '0', '1'],
                ['1', '1', '0', '1']]
    conv_bin_list = [['0', '0', '0', '1'],
                     ['0', '0', '0', '1']] 
    row = 0
    col = 1
    assert f.convert_filled_adjacent(row,
                                     col,
                                     bin_list) == conv_bin_list

    bin_list = [['0', '1', '0', '0'],
                ['1', '0', '0', '0']]
    conv_bin_list = [['0', '0', '0', '0'],
                     ['1', '0', '0', '0']]
    row = 0
    col = 1 
    assert f.convert_filled_adjacent(row,
                                     col,
                                     bin_list) == conv_bin_list


def test_count_groups():
    bin_list = [['0', '1', '0', '1'],
                ['1', '1', '0', '1']]
    assert f.count_groups(bin_list) == 2

    bin_list = [['0', '1', '0', '0'],
                ['1', '0', '0', '0']]
    assert f.count_groups(bin_list) == 2

    bin_list = [['0', '1', '0', '1'],
                ['1', '0', '0', '0']]
    assert f.count_groups(bin_list) == 3

    bin_list = [['0', '1', '1', '1', '0'],
                ['1', '0', '0', '0', '0']]
    assert f.count_groups(bin_list) == 2

    bin_list = [['0', '1', '1', '1', '0'],
                ['1', '0', '0', '0', '0'],
                ['1', '0', '0', '0', '1']]
    assert f.count_groups(bin_list) == 3

    bin_list = [['0', '0', '0', '0', '1'],
                ['0', '0', '0', '0', '1'],
                ['1', '1', '1', '1', '1']]
    assert f.count_groups(bin_list) == 1

    bin_list = [['0', '1', '0', '0', '0'],
                ['0', '0', '1', '0', '1'],
                ['1', '1', '1', '1', '1']]
    assert f.count_groups(bin_list) == 2

    bin_list = [['1', '0', '0', '0'],
                ['0', '1', '0', '1'],
                ['1', '1', '1', '1']]
    assert f.count_groups(bin_list) == 2
