import pytest
import day_20171216 as s


def test_spin():
    group = ['a', 'b', 'c', 'd', 'e'] 
    size = 1
    spun_group = ['e', 'a', 'b', 'c', 'd'] 
    assert s.spin(group, size) == spun_group

    group = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'] 
    size = 1
    spun_group = ['p', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'] 
    assert s.spin(group, size) == spun_group


def test_get_positions():
    x_move = '1/15'
    assert s.get_positions(x_move) == [1, 15]


def test_exchange():
    group = ['a', 'b', 'c', 'd', 'e'] 
    positions = [1, 3]
    x_group = ['a', 'd', 'c', 'b', 'e']
    assert s.exchange(group, positions) == x_group


def test_get_partner_positions():
    p_move = 'b/e'
    group = ['a', 'd', 'c', 'b', 'e']
    assert s.get_partner_positions(group, p_move) == [3, 4]
