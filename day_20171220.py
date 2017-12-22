#!/usr/bin/env python3
"""
AoC solution day 20
"""

import re


def distance(particle):
    d = abs(particle['p']['X']) + abs(particle['p']['Y']) + abs(particle['p']['Z'])
    return d


def parse_line(l):
    capture = None
    parts = "(\w=<(-?\d+),\s?(-?\d+),\s?(-?\d+)>,?\s?)"
    captures = re.findall(parts, l)
    position = {
        'X': int(captures[0][1]),
        'Y': int(captures[0][2]),
        'Z': int(captures[0][3])
    }

    velocity = {
        'X': int(captures[1][1]),
        'Y': int(captures[1][2]),
        'Z': int(captures[1][3])
    }

    acceleration = {
        'X': int(captures[2][1]),
        'Y': int(captures[2][2]),
        'Z': int(captures[2][3])
    }

    particle = {
        'p': position,
        'v': velocity,
        'a': acceleration}

    particle['d'] = distance(particle)

    return particle
    

def update(particle):
    particle['v']['X'] += particle['a']['X']
    particle['v']['Y'] += particle['a']['Y']
    particle['v']['Z'] += particle['a']['Z']

    particle['p']['X'] += particle['v']['X']
    particle['p']['Y'] += particle['v']['Y']
    particle['p']['Z'] += particle['v']['Z']

    particle['d'] = distance(particle)

    return particle


def get_distances(particles, ticks):
    for tick in range(ticks):
        particles = [update(particle) for particle in particles]

    distances = [p['d'] for p in particles]
    return distances, particles


if __name__ == '__main__':
    lines = []
    with open('data/input_data_20171220.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))

    particles = [parse_line(line) for line in lines]
    ticks = 100000
    distances, u_particles = get_distances(particles, ticks)
    min_d = distances.index(min(distances))
    print(distances)
    print('---------------------------')
    print('min distance index: ', min_d)
    print('distance: {}'.format(u_particles[min_d]['d']))
