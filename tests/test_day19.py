import pytest
import day_20171219 as n

def test_crossroad():
    tracker = {
        'x': 1,
        'y': 2,
        'direction': 'S',
        'current': '+',
        'letters': []
    }
    maze = [[' ', '|', ' '],
            [' ', '|', ' '],
            [' ', '+', '-'],
            [' ', ' ', ' ']
            ]
    new_tracker = {
        'x': 2,
        'y': 2,
        'direction': 'E',
        'current': '-',
        'letters': []
    }
    assert n.crossroad(tracker, maze) == new_tracker

    tracker = {
        'x': 1,
        'y': 2,
        'direction': 'W',
        'current': '+',
        'letters': []
    }
    maze = [[' ', '|', ' '],
            [' ', '|', ' '],
            [' ', '+', '-'],
            [' ', ' ', ' ']
            ]
    new_tracker = {
        'x': 1,
        'y': 1,
        'direction': 'N',
        'current': '|',
        'letters': []
    }
    assert n.crossroad(tracker, maze) == new_tracker
