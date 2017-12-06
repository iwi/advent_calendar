#!/usr/bin/env python3
"""
"""

import csv

# Part one
def count_steps_to_exit(maze):
    location = 0
    steps = 0
    print(maze[location][0])
    ll = [location]
    while (location < len(maze)) & (location >= 0):
        # print('step: ', steps)
        change = int(maze[location][0])
        # print('change: ', change)
        maze[location][0] += 1
        location = location + change
        ll.append(location)
        # print('location', location)
        steps += 1

    print(ll)
    return steps


def count_steps_to_exit_2(maze):
    location = 0
    steps = 0
    ll = [location]
    while (location < len(maze)) & (location >= 0):
        change = int(maze[location][0])
        if change < 3:
            maze[location][0] += 1
        else:
            maze[location][0] -= 1
        location = location + change
        ll.append(location)
        steps += 1

    print(ll)
    return steps


if __name__ == '__main__':
    maze = []
    with open('data/input_data_20171205.csv', 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for element in data:
            maze.append(element)

        print('steps: ', count_steps_to_exit(maze))
        print('steps: ', count_steps_to_exit_2(maze))
        print('trial steps: ', count_steps_to_exit([[0], [3], [0], [1], [-3]]))
        print('trial steps 2: ', count_steps_to_exit_2([[0], [3], [0], [1], [-3]]))
