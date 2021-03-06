#!/usr/bin/env python3
"""
AoC solution day 12
2017-12-12
"""

def get_connected_to(program, connected, group):
    if program is None:
        return group

    group.append(program)

    for sub_program in connected[program]:
        if sub_program not in group:
            group = get_connected_to(sub_program, connected, group)

    return group


if __name__ == '__main__':
    connections = []
    with open('data/input_data_20171212.txt', 'r') as f:
           for line in f:
               connections.append(line.rstrip())

    conns = [conn.split() for conn in connections]
    connected = []
    for c in conns:
        clean = []
        for prog in c[2:]:
            clean.append(int(prog.rstrip(',')))
        connected.append(clean)

    gs = []
    cumm_groups = []

    for program in range(len(conns)):
        if program not in cumm_groups:
            gs.append(get_connected_to(program, connected, []))
        cumm_groups = set(sum(gs, []))

    print(gs)
    print('number of groups: ', len(gs))

    group = []
    group = get_connected_to(0, connected, group)
    print('group: ', group)
    print('number of elements: ', len(group))
