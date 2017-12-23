#!/usr/bin/env python3
"""
AoC solution day 20
"""

import re


def distance(particle):
    d = abs(particle['p']['X']) + abs(particle['p']['Y']) + abs(particle['p']['Z'])
    return d


def parse_line(l, index):
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
    particle['index'] = index
    particle['alive'] = True

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


def sorter(particles):
    sorted_particles = sorted(particles,
                              key= lambda k: (k['p']['X'],
                                              k['p']['Y'],
                                              k['p']['Z']))
    return sorted_particles
                            

def are_equal(p1, p2):
    return (p1['X'] == p2['X']) & \
           (p1['Y'] == p2['Y']) & \
           (p1['Z'] == p2['Z'])


def detect_colliders_sorted(particles):
    for index, particle in enumerate(particles):
        if index < (len(particles) - 1):
            pos1 = particle['p']
            pos2 = particles[index + 1]['p']
            if are_equal(pos1, pos2):
                particle['alive'] = False
                particles[index + 1]['alive'] = False
    return particles


def remove_colliding_sorted(particles):
    indices = []
    for index, particle in enumerate(particles):
        if not particle['alive']:
            indices.append(index)
    for index in sorted(indices, reverse=True):
        particles.pop(index)
    return particles


def simplify_colliding_sorted(particles):
    particles = detect_colliders_sorted(particles)
    particles = remove_colliding_sorted(particles)
    return particles


def remove_colliding(particles):
    sorted_particles = sorter(particles)
    simplified_particles = simplify_colliding_sorted(sorted_particles)
    return simplified_particles


def get_distances(particles, ticks):
    for tick in range(ticks):
        particles = [update(particle) for particle in particles]
        particles = remove_colliding(particles)
        print(len(particles))

    distances = [p['d'] for p in particles]
    return distances, particles


if __name__ == '__main__':
    lines = []
    with open('data/input_data_20171220.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))

    particles = [parse_line(line, index) for index, line in enumerate(lines)]
    ticks = 10000
    distances, u_particles = get_distances(particles, ticks)
    min_d = distances.index(min(distances))
    print('min distance index: ', min_d)
    print('distance: {}'.format(u_particles[min_d]['d']))
