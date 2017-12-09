#!/usr/bin/env python3
"""
AoC solution day seven 
2017-12-07
badly finished!!!!!!!!!!!!!!!!
"""
import re
import statistics as st

# Part 1
def parse_disk_info(disk_record):
    return(disk_record.split())


def get_disk_names(disk_structure):
    return [parse_disk_info(element)[0] for element in disk_structure]
    

def parse_csv(disks_csv):
    return disks_csv.split(',')


def get_higher_level_disks(disks_info):
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


def get_children(disk, disks_info):
    children = []
    for index, row in enumerate(disks_info):
        if row[0] == disk:
            break
    for i, element in enumerate(row):
        if element == '->':
            for j in range(i + 1, len(row)):
                children.append(row[j].rstrip(','))  
            break
    return(children)


def get_all_children(disk, disks_info):
    grand_children = []
    children = get_children(disk, disks_info)
    if len(children) is not 0:
        for child in children:
            for grandchild in get_all_children(child, disks_info):
                if len(grandchild) is not 0:
                    grand_children.append(grandchild)
        for grandchild in grand_children:
            children.append(grandchild)
    return children


def weigh_disks(disks, disk_list):
    weight = 0
    if type(disks) == 'str':
        return disk_list[disks]

    for disk in disks:
        weight += disk_list[disk] 
    return weight


def find_different_element(elements):
    if len(elements) < 3:
        return 0

    if elements[0] == elements[1]:
        truth = elements[0]
    elif elements[0] == elements[2]:
        truth = elements[0]
    else:
        return 0

    for index, element in enumerate(elements):
        if element != elements[0]:
            return index

    return None


def compare_children_weight(parent, disk_list, disks_info):
    children = get_children(parent, disks_info)
    weights = []
    for child in children:
        grandchildren = get_all_children(child, disks_info)
        grandchildren.append(child)
        weight = weigh_disks(grandchildren, disk_list)
        print(weight)
        weights.append(weight)

    if len(weights) == 0:
        return children, None, 0

    if max(weights) != st.mean(weights):
        index = find_different_element(weights)
        if index > 0:
            difference = weights[index] - weights[0]
            return children, index, difference
        elif index == 0:
            difference = weights[0] - weights[1]
            return children, index, difference

    return children, None, 0


def get_wrong_weight_difference(disks_info):
    disk_list = build_disks_list(disks_info)
    bottom_disk = 'eqgvf'
    comparison = compare_children_weight(bottom_disk, disk_list, disks_info)
    if comparison[2] != 0:
        for child in comparison[0]:
            comparison = get_wrong_weight_difference(child, disk_list, disks_info)
            return disk_list[comparison[0][comparison[1]]]

    print(comparison)

    return comparison



if __name__ == '__main__':
    disk_structure = []
    with open('data/input_data_20171207.txt', 'r') as f:
           for line in f:
               disk_structure.append(line.rstrip())

    disks_info = [parse_disk_info(disks_info) for disks_info in disk_structure]

    print('bottom disk: ', get_bottom_disk_name(disk_structure))
    print('the difference of the wrong weight is ', get_wrong_weight_difference(disk_structure))
