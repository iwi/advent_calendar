#!/usr/bin/python

import sys

from collections import defaultdict
from optparse import OptionParser

def main():
    lines = []
    with open('data/input_data_20171218.txt', 'r') as f:
        for line in f:
            lines.append(line.rstrip('\n'))

    regs = [defaultdict(lambda: 0), defaultdict(lambda: 0)]

    vals = [0] * 2
    pc = [0] * 2
    queue = [[], []]
    for p in [0, 1]:
        regs[p]['p'] = p
    cnt = [0] * 2
    waiting = [False] * 2
    while not all(waiting) and all([pc[p] < len(lines) for p in [0, 1]]):
        for p in [0, 1]:
            line = lines[pc[p]]
            instr = line.split(' ')[0]
            args = line.split(' ')[1:]
            for i, arg in enumerate(args):
                if arg.isalpha():
                    vals[i] = regs[p][arg]
                else:
                    vals[i] = int(arg)
            if instr == 'snd':
                queue[1 - p].append(vals[0])
                cnt[p] += 1
            elif instr == 'set':
                regs[p][args[0]] = vals[1]
            elif instr == 'add':
                regs[p][args[0]] += vals[1]
            elif instr == 'mul':
                regs[p][args[0]] *= vals[1]
            elif instr == 'mod':
                regs[p][args[0]] = vals[0] % vals[1]
            elif instr == 'rcv':
                if len(queue[p]) == 0:
                    waiting[p] = True
                    continue
                waiting[p] = False
                regs[p][args[0]] = queue[p].pop(0)
            elif instr == 'jgz':
                if vals[0] > 0:
                    pc[p] += vals[1]
                    continue
            else:
                raise
            pc[p] += 1

    print cnt[1]

# Python trick to get a main routine
if __name__ == "__main__":
    main()
