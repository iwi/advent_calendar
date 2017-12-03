#!/usr/bin/env python3

# 2017-12-01
def sum_repeats(number, lag):
    first = number[0:lag]
    second = number[lag:len(number)]
    lagged = second + first
    repeats = [(int(y) if (x == y) else 0) for x, y in zip(lagged, number)]
    total = sum(repeats)
    print(total)
    return(total)  # returning it so it can be tested

if __name__ == '__main__':
    with open('data/input_data.txt', 'r') as f:
        number = f.read().rstrip()
        
        sum_repeats(number, 1)
        sum_repeats(number, int(len(number) / 2))
