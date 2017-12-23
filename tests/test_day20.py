import pytest
import day_20171220 as t

def test_parse_line():
    line = 'p=<-2286,-1779,-461>, v=<-327,-255,-65>, a=<22,23,2>'
    index = 2
    assert t.parse_line(line, index)['p']['X'] == -2286


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
    

def test_sorter():
    unsorted = [{'p': {'Y': 0, 'X': 1, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3},
                {'p': {'Y': 1, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3}]
    sorted = [{'p': {'Y': 0, 'X': 1, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3},
                {'p': {'Y': 1, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3}]
    assert t.sorter(unsorted) == sorted

def test_are_equal():
    p1 = {'X': 1, 'Y': 2, 'Z': 3}
    p2 = {'X': 1, 'Y': 2, 'Z': 3}
    assert t.are_equal(p1, p2) is True

    p1 = {'X': 1, 'Y': 2, 'Z': 3}
    p2 = {'X': 0, 'Y': 2, 'Z': 3}
    assert t.are_equal(p1, p2) is False


def test_detect_collider_sorted():
    particles = [{'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 0,
                'alive': True},
                {'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 1, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 2,
                'alive': True},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 1,
                'alive': True}]
    simplified = [{'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 0,
                'alive': False},
                {'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 1, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 2,
                'alive': False},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 1,
                'alive': True}]
    assert t.detect_colliders_sorted(particles) == simplified


def test_simplify_colliding_sorted():
    particles = [{'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 0,
                'alive': True},
                {'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 1, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 2,
                'alive': True},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 1,
                'alive': True}]
    simplified = [{'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 1,
                'alive': True}]
    assert t.simplify_colliding_sorted(particles) == simplified


def test_remove_colliding():
    particles = [{'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 1, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 2,
                'alive': True},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 1,
                'alive': True},
                {'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 1, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 0,
                'alive': True}]
    simplified = [{'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 1,
                'alive': True}]
    assert t.remove_colliding(particles) == simplified

    particles = [{'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 1, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 2,
                'alive': True},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 2,
                'index': 1,
                'alive': True},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 1,
                'index': 0,
                'alive': True},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 3,
                'alive': True},
                {'p': {'Y': 1000, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 5,
                'alive': True},
                {'p': {'Y': 1001, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 4,
                'alive': True},
                {'p': {'Y': 0, 'X': 0, 'Z': 0},
                'v': {'Y': 1, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 7,
                'alive': True}]
    simplified = [{'p': {'Y': 1001, 'X': 100, 'Z': 2},
                'v': {'Y': 6, 'X': 7, 'Z': 8},
                'a': {'Y': 3, 'X': 4, 'Z': 5},
                'd': 3,
                'index': 4,
                'alive': True}]
    assert t.remove_colliding(particles) == simplified

