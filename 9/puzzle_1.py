#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append(int(l))

preamble_length = 25

invalid_number = 0
for i in range(preamble_length, len(puzzle_input)):
    current = puzzle_input[i]
    prior = puzzle_input[i-preamble_length:i]
    components = []
    for n, b in enumerate([(n in prior) for n in [current - n for n in prior]]):
        if (b and prior[n] != current/2):
            components.append(prior[n])

    if len(components) < 2:
        print("\t{} is not valid".format(current))
        invalid_number = current
    else:
        print("{} is valid ({}+{})".format(current, components[0], components[1]))
        

print("The invalid number is {}".format(invalid_number))

for window_size in range(2, len(puzzle_input)):
    for i in range(0, len(puzzle_input)):
        if (window_size+i <= len(puzzle_input)):
            if sum(puzzle_input[i:window_size+i]) == invalid_number:
                min_value = min(puzzle_input[i:window_size+i])
                max_value = max(puzzle_input[i:window_size+i])
                product_value = min_value+max_value
                print("The encryption weakness is: {} ({}+{})".format(product_value, min_value, max_value))
                exit()