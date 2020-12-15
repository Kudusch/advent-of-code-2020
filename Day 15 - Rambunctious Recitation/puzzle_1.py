#!/usr/bin/env python
# -*- coding: utf-8 -*-


# read puzzle input
puzzle_input = "12,1,16,3,11,0"
#puzzle_input = "0,3,6"
puzzle_input = [int(i) for i in puzzle_input.split(",")]

numbers_said = {}
for i, e in enumerate(puzzle_input):
    numbers_said[int(e)] = i+1

next_said = 0

for i in range(len(numbers_said), 30000001):
#for i in range(len(numbers_said), 2021):
    last_said = next_said
    if (i)%300000 == 0:
        print("\rProgress:", int(i/300000), "/ 100", end = "")
    
    if last_said in numbers_said:
        next_said = i - numbers_said[last_said]
    else:
        next_said = 0

    numbers_said[last_said] = i
    if i == 2020:
        print("\n\nStep {}: {}".format(i, last_said))        


print("\n\nStep {}: {}".format(i, last_said))