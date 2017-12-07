#!/usr/bin/env python3
"""
AoC solution day seven 
2017-12-07
"""
import re

# Part 1
def parse_disk_info(disk_info):
    return(disk_info.split())


def get_disk_names(disk_structure):
    return [parse_disk_info(element)[0] for element in disk_structure]
    

def parse_csv(disks_csv):
    return disks_csv.split(',') 


def get_higher_level_disks(disk_structure):
    higher_disks = []
    disks_info = [parse_disk_info(disk_info) for disk_info in disk_structure]
    for disk_record in disks_info:
        for index, element in enumerate(disk_record):
            if element == '->':
                for i in range(index + 1, len(disk_record)):
                    higher_disks.append(disk_record[i].rstrip(','))  
                break

    return list(set(higher_disks))


def get_bottom_disk_name(disk_structure):
    disks = get_disk_names(disk_structure)
    higher_level_disks = get_higher_level_disks(disk_structure)
    for disk in disks:
        if disk not in higher_level_disks:
            return disk


if __name__ == '__main__':
    disk_structure = []
    with open('data/input_data_20171207.txt', 'r') as f:
           for line in f:
               disk_structure.append(line.rstrip())

    print('bottom disk: ', get_bottom_disk_name(disk_structure))
