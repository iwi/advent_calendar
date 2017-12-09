#!/usr/bin/env python3
"""
AoC solution day eight
2017-12-08
"""
import re

# Part 1
def prepare_instructions(instructions):
    for inst in instructions:
        inst[6] = int(inst[6])
        if inst[1] == 'dec':
            inst[2] = -int(inst[2])
        else:
            inst[2] = int(inst[2])

    return instructions

def build_registers_list(instructions):
    registers = {}
    for inst in instructions:
        registers.update({inst[0]: 0})
    return registers


def operate(operation, x, y):
    return {
        '==': lambda x, y: x == y,
        '>': lambda x, y: x > y,
        '>=': lambda x, y: x >= y,
        '<': lambda x, y: x < y,
        '<=': lambda x, y: x <= y,
        '!=': lambda x, y: x != y}[operation](x, y)


def condition(registers, inst):
    name = inst[4]
    operation = inst[5]
    value = inst[6]
    return operate(operation, registers[name], value)


def interpret(registers, inst):
    name = inst[0]
    change = inst[2]
    if condition(registers, inst):
        registers.update({name: registers[name] + change})
    return registers


def update_registers(registers, instructions):
    for inst in instructions:
        registers = interpret(registers, inst)
    return registers


if __name__ == '__main__':
    instructions = []
    with open('data/input_data_20171208.txt', 'r') as f:
           for line in f:
               instructions.append(line.rstrip())

    instructions = [inst.split() for inst in instructions]
    instructions = prepare_instructions(instructions)
    registers = build_registers_list(instructions)

    registers = update_registers(registers, instructions) 
    mx = max(registers, key=registers.get)
    print(registers)
    print(registers[mx])

