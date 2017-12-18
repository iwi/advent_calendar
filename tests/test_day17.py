import pytest
import day_20171217 as s


def test_add_lock():
    initial_spinlock = [0, 1, 2, 3, 4, 5]
    steps = 3
    position = 1
    final_position = 5
    final_spinlock = [0, 1, 2, 3, 4, 6, 5]
    assert s.add_lock(initial_spinlock, steps, position) == (final_spinlock, final_position)
    
    initial_spinlock = [0, 1, 2, 3, 4]
    steps = 7
    position = 3
    final_position = 1
    final_spinlock = [0, 5, 1, 2, 3, 4]
    assert s.add_lock(initial_spinlock, steps, position) == (final_spinlock, final_position)

    initial_spinlock = [0]
    steps = 3
    position = 0
    final_position = 1
    final_spinlock = [0, 1]
    assert s.add_lock(initial_spinlock, steps, position) == (final_spinlock, final_position)
