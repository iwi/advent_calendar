#!/usr/bin/env python3
"""
AoC solution day 19
"""

def crossroad(tracker, maze):
    x = tracker['x']
    # print('x: ', x)
    y = tracker['y']
    # print('y: ', y)
    direction = tracker['direction']
    if direction == 'S':
        if maze[y + 1][x] != ' ':
            y += 1
            tracker['direction'] = 'S'
        elif maze[y][x + 1] != ' ':
            x += 1 
            tracker['direction'] = 'E'
        elif maze[y][x - 1] != ' ':
            x -= 1 
            tracker['direction'] = 'W'
    elif direction == 'E':
        if maze[y][x + 1] != ' ':
            x += 1
            tracker['direction'] = 'E'
        elif maze[y - 1][x] != ' ':
            y -= 1 
            tracker['direction'] = 'N'
        elif maze[y + 1][x] != ' ':
            y += 1 
            tracker['direction'] = 'S'
    elif direction == 'N':
        if maze[y - 1][x] != ' ':
            y -= 1
            tracker['direction'] = 'N'
        elif maze[y][x + 1] != ' ':
            x += 1 
            tracker['direction'] = 'E'
        elif maze[y][x - 1] != ' ':
            x -= 1 
            tracker['direction'] = 'W'
    elif direction == 'W':
        if maze[y][x - 1] != ' ':
            x -= 1
            tracker['direction'] = 'W'
        elif maze[y - 1][x] != ' ':
            y -= 1 
            tracker['direction'] = 'N'
        elif maze[y + 1][x] != ' ':
            y += 1 
            tracker['direction'] = 'S'
    else:
        print('I need a wind')
    tracker['x'] = x
    tracker['y'] = y
    tracker['current'] = maze[y][x]
    return tracker


def move(tracker, maze):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                'Y', 'Z']
    current = tracker['current']
    direction = tracker['direction']
    if current != '+':
        if direction == 'S':
            tracker['y'] += 1
        elif direction == 'E':
            tracker['x'] += 1
        elif direction == 'N':
            tracker['y'] -= 1
        elif direction == 'W':
            tracker['x'] -= 1
        tracker['current'] = maze[tracker['y']][tracker['x']]
    elif current == '+':
        tracker = crossroad(tracker, maze)

    if tracker['current'] in alphabet:
        tracker['letters'].append(tracker['current'])

    if tracker['current'] == ' ':
        tracker['current'] = 'end'
            
    return tracker


def follow_path(tracker, maze):
    while tracker['current'] != 'end':
        tracker = move(tracker, maze)
        print('x: ', tracker['x'])
        print('y: ', tracker['y'])
    return tracker
    

if __name__ == '__main__':
    maze = []
    with open('data/input_data_20171219.txt', 'r') as f:
        for line in f:
            maze.append(list(line.rstrip('\n')))

    tracker = {
        'x': 153,
        'y': 0,
        'direction': 'S',
        'current': '|',
        'letters': []
    }

    tracker = follow_path(tracker, maze)
    print('the captured letters are {}'.format(tracker['letters']))

