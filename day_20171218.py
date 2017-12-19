#!/usr/bin/env python3
"""
AoC solution day 18
"""

def get_val(value_string, status):
    try:
        value_int = int(value_string)
    except:
        value_int = status['registers'][value_string] 
    return value_int


def initialise_register(name, status):
    try:
        value = status['registers'][name]
    except:
        status['registers'][name] = 0
    return status


def apply_snd(instruction, status):
    name = instruction[1]
    status = initialise_register(name, status)
    status['last_played'] = status['registers'][name]
    return status


def apply_set(instruction, status):
    name = instruction[1]
    status = initialise_register(name, status)
    value = get_val(instruction[2], status)
    status['registers'][name] = value
    return status


def apply_add(instruction, status):
    name = instruction[1]
    status = initialise_register(name, status)
    value = get_val(instruction[2], status)
    status['registers'][name] += value
    return status


def apply_mul(instruction, status):
    name = instruction[1]
    status = initialise_register(name, status)
    value = get_val(instruction[2], status)
    status['registers'][name] *= value
    return status


def apply_mod(instruction, status):
    name = instruction[1]
    status = initialise_register(name, status)
    value = get_val(instruction[2], status)
    status['registers'][name] = status['registers'][name] % value
    return status


def apply_rcv(instruction, status):
    name = instruction[1]
    status = initialise_register(name, status)
    if status['registers'][name] == 0:
        return status
    status['recovered'] = status['last_played'] 
    return status


def apply_jgz(instruction, status):
    name_X = instruction[1]
    status = initialise_register(name_X, status)
    name_Y = instruction[2]
    status = initialise_register(name_Y, status)
    val_Y = get_val(name_Y, status)
    if status['registers'][name_X] <= 0:
        return 1
    return val_Y


def run_instructions(instructions, status):
    index = 0
    while (index >= 0) and (index < len(instructions)) and (status['recovered'] is None):
        print('index: {}'.format(index))
        instruction = instructions[index]
        type = instruction[0]
        if type == 'set':
            status = apply_set(instruction, status)
            index += 1
        elif type == 'add':
            status = apply_add(instruction, status)
            index += 1
        elif type == 'mul':
            status = apply_mul(instruction, status)
            index += 1
        elif type == 'mod':
            status = apply_mod(instruction, status)
            index += 1
        elif type == 'rcv':
            status = apply_rcv(instruction, status)
            index += 1
        elif type == 'jgz':
            jump = apply_jgz(instruction, status)
            index += jump        
        elif type == 'snd':
            status = apply_snd(instruction, status)
            index += 1
    return status


if __name__ == '__main__':
    instructions = []
    with open('data/input_data_20171218.txt', 'r') as f:
           for line in f:
               instructions.append(line.strip().split(" "))
    status = {
        'last_played': None,
        'recovered': None,
        'registers': {}} 
    status = run_instructions(instructions, status)
    print(status)
    
            



