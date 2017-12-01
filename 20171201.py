#!/usr/bin/env python3

# Answer for the first of december

f = open('input_data.txt', 'r')

number = f.read()

number_list = list(number.rstrip())

original = number_list[:]

first = number_list.pop(0)

number_list.append(first)

number_list_diff = list(map((lambda x, y: x == y), original, number_list))

repeats = list(map((lambda x, y: (int(y) if x else 0)), number_list_diff, original))

total = sum(repeats)

print(total)


# second part

list_length = len(number_list)

number_list = original[:]

first_part = number_list[0:int(list_length / 2)]
second_part = number_list[int(list_length/2):list_length]

composite = second_part + first_part

number_list_diff = list(map((lambda x, y: x == y), original, composite))

repeats = list(map((lambda x, y: (int(y) if x else 0)), number_list_diff, original))

total = sum(repeats)

print(total)

