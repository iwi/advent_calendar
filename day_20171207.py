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


def get_higher_level_disks(disk_info):
    higher_disks = []
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


# part 2
def remove_brackets(bracketed_number):
    expression = "(\d+)"
    captures = re.search(expression, bracketed_number)
    return captures.group(0)


def build_disks_list(disks_info):
    disk_list = {}
    for disk_record in disks_info:
        disk_list.update({disk_record[0]: int(remove_brackets(disk_record[1]))})
    return disk_list


def get_children(disk, disk_info):
    children = []
    for index, row in enumerate(disk_info):
        if row[0] == disk:
            break
    for i, element in enumerate(row):
        if element == '->':
            for j in range(i + 1, len(row)):
                children.append(row[j].rstrip(','))  

            break

    return(children)


if __name__ == '__main__':
    disk_structure = []
    with open('data/input_data_20171207.txt', 'r') as f:
           for line in f:
               disk_structure.append(line.rstrip())

    disks_info = [parse_disk_info(disk_info) for disk_info in disk_structure]

    print('bottom disk: ', get_bottom_disk_name(disk_structure))
    print('the difference of the wrong weight is ', get_wrong_weight_difference(disk_structure))
