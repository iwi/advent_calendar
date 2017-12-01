#!/usr/bin/env python3

# 2017-12-01
# First part

f = open('input_data.txt', 'r')
number = f.read().rstrip()
first = number[0]
second = number[1:len(number)]
lagged = second + first
diff = [x == y for x, y in zip(number, lagged)]
repeats = [(int(y) if x else 0) for x, y in zip(diff, number)]
total = sum(repeats)
print(total)

# Second part
list_length = len(number)
first = number[0:int(list_length / 2)]
second = number[int(list_length/2):list_length]
lagged = second + first
diff = [x == y for x, y in zip(number, lagged)]
repeats = [(int(y) if x else 0) for x, y in zip(diff, number)]
total = sum(repeats)
print(total)

