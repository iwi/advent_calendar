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
        if (status['program'] == 1) and (name == 'p'):
            status['registers']['p'] = 1
        else:
            status['registers'][name] = 0
    return status


def apply_snd(instruction, status1, status2):
    name = instruction[1]
    status1 = initialise_register(name, status1)
    status1['sent_counter'] += 1
    status2['queue'].append(status1['registers'][name]) 
    return status1, status2


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


def apply_rcv(index, instruction, status):
    name = instruction[1]
    status = initialise_register(name, status)
    if status['queue'] != []:
        status['registers'][name] = status['queue'].pop(0)
        index += 1
    else:
        status['waiting'] = True
    return status, index


def apply_jgz(instruction, status):
    name_X = instruction[1]
    status = initialise_register(name_X, status)
    name_Y = instruction[2]
    val_Y = get_val(name_Y, status)
    if status['registers'][name_X] <= 0:
        return 1
    return val_Y


def evaluate(index, instruction, status1, status2):
    type = instruction[0]
    if type == 'set':
        status1 = apply_set(instruction, status1)
        index += 1
    elif type == 'add':
        status1 = apply_add(instruction, status1)
        index += 1
    elif type == 'mul':
        status1 = apply_mul(instruction, status1)
        index += 1
    elif type == 'mod':
        status1 = apply_mod(instruction, status1)
        index += 1
    elif type == 'jgz':
        jump = apply_jgz(instruction, status1)
        index += jump
    elif type == 'snd':
        status1, status2 = apply_snd(instruction, status1, status2)
        index += 1
    elif type == 'rcv':
        status1, index = apply_rcv(index, instruction, status1)
    return index, status1, status2


def verify_waiting(status):
    if status['queue'] != []:
        status['waiting'] = False
    return status


def run_instructions(instructions, status_P0, status_P1):
    index_P0 = 0
    index_P1 = 0
    deadlock = False
    n = 0
    while not deadlock and n < 1000:
        n += 1
        instruction_P0 = instructions[index_P0]
        print('inst 0: ', instruction_P0)
        if not status_P0['waiting']:
            index_P0, status_P0, status_P1 = evaluate(index_P0, instruction_P0, status_P0, status_P1)
        if index_P0 not in range(0, len(instructions)): 
            status_P0['terminated'] = True

        instruction_P1 = instructions[index_P1]
        print('inst 1: ', instruction_P1)
        if not status_P1['waiting']:
            index_P1, status_P1, status_P0 = evaluate(index_P1, instruction_P1, status_P1, status_P0)
            print('sent counter p1 ',status_P1['sent_counter'])
        if index_P1 not in range(0, len(instructions)):
            status_P1['terminated'] = True
        print('i0', index_P0)
        print('i1', index_P1)
        print('status0 ', status_P0)
        print('status1 ', status_P1)

        status_P0 = verify_waiting(status_P0)
        status_P1 = verify_waiting(status_P1)
        deadlock = (status_P0['waiting'] and status_P1['waiting']) or \
                (status_P0['terminated'] or status_P1['terminated'])

    return status_P0, status_P1


if __name__ == '__main__':
    instructions = []
    with open('data/input_data_20171218.txt', 'r') as f:
    # with open('data/test_day18.txt', 'r') as f:
           for line in f:
               instructions.append(line.strip().split(" "))
    status_P0 = {
        'program': 0,
        'terminated': False,
        'waiting': False,
        'sent_counter': 0,
        'queue': [],
        'registers': {}} 
    status_P1 = {
        'program': 1,
        'terminated': False,
        'waiting': False,
        'sent_counter': 0,
        'queue': [],
        'registers': {}} 
    
    status_P0, status_P1 = run_instructions(instructions, status_P0, status_P1)
    print('The number of times program 1 sent a message was {}'.format(status_P1['sent_counter']))
