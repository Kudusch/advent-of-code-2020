#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append({"pattern":l.strip(), "length":len(l)})

slope = {"x":3, "y":1}

for step in range(1, len(puzzle_input), slope["y"]):
    