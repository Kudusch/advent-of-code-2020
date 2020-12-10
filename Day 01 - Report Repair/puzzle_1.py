#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append(int(l))

# test for all combinations of size 2
for c in list(itertools.combinations(puzzle_input, 2)):
    if sum(c) == 2020:
        print(c)
        print(c[0] * c[1])

# test for all combinations of size 3
for c in list(itertools.combinations(puzzle_input, 3)):
    if sum(c) == 2020:
        print(c)
        print(c[0] * c[1] * c[2])