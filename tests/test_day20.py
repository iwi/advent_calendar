import pytest
import day_20171220 as t

def test_parse_line():
    line = 'p=<-2286,-1779,-461>, v=<-327,-255,-65>, a=<22,23,2>'
    assert t.parse_line(line)['p']['X'] == -2286


def test_update():
    particle = {'p': {'Y': 0, 'X': 1, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3}
    u_partic = {'p': {'Y': 9, 'X': 12, 'Z': 15},
                'v': {'Y': 9, 'X': 11, 'Z': 13},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 36}
    assert t.update(particle) == u_partic
    
