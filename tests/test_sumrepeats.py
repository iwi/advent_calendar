import pytest
import day_20171201 as one

def test_sum_repeats():
    data = '12231'
    lag = 1
    assert one.sum_repeats(data, lag) == 3
