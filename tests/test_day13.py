import pytest
import day_20171213 as th

def test_get_scanner_position():
    t = 11
    rg = 4
    assert th.get_scanner_position(t, rg) == 1
    t = 4
    rg = 4
    assert th.get_scanner_position(t, rg) == 2
    t = 12
    rg = 4
    assert th.get_scanner_position(t, rg) == 0
    t = 12
    rg = 7
    assert th.get_scanner_position(t, rg) == 0
