#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append({"pattern":l.strip(), "length":len(l.strip())})


solution = 1
slopes = [
    {"x":1, "y":1},
    {"x":3, "y":1}, # first puzzle
    {"x":5, "y":1},
    {"x":7, "y":1},
    {"x":1, "y":2}
]
for slope in slopes:
    n_trees = 0
    for step_x, step_y in enumerate(range(slope["y"], len(puzzle_input), slope["y"])):
        x = ((step_x + 1) * slope["x"])+1
        y = step_y
        
        char_index = ((x-1) % puzzle_input[y]["length"])
        char = puzzle_input[y]["pattern"][char_index]
        if (char == "#"):
            n_trees += 1

    print("You encounter {} trees with the slope {}".format(n_trees, slope))
    solution = solution * n_trees

print("\nThe solution is {}".format(solution))