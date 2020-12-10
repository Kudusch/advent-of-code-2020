#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import compress

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append(l.strip())

# 128 rows, 7 steps
# F = lower half
# B = upper half
# 8 columns, 3 steps
# L = lower half
# R = upper half

rows = list(range(0, 128))
cols = list(range(0, 8))

def bin_partition(l, i):
    if len(l) > 1:
        if (cur_instructions[i] in ["F", "L"]):
            return(bin_partition(l[:int(len(l)/2)], i+1))
        elif (cur_instructions[i] in ["B", "R"]):
            return(bin_partition(l[int(len(l)/2):], i+1))
    else:
        return(l[0])

seat_ids = []
row_numbers = []
for instructions in puzzle_input:
    # rows
    cur_instructions = instructions[0:7]
    row = bin_partition(rows, 0)
    # cols
    cur_instructions = instructions[7:]
    col = bin_partition(cols, 0)
    sid = (row * 8) + col
    seat_ids.append(sid)
    
    if row == 0 or row == 127:
        row_numbers.append(False)
    else:
        row_numbers.append(True)
    
    print("Seat with instructions {} is at row {} and col {} (sead id: {})".format(
        instructions,
        row,
        col,
        sid
    ))

seat_ids.sort()

seat_ids_delta = [((seat_ids[i-1])-x) for i, x in enumerate(seat_ids)]
index_id = seat_ids_delta.index(-2)

seat_ids.sort()
print("\nThe highest seat id is: {}".format(seat_ids[-1]))


print("You sit between seat {} and {}".format(*seat_ids[index_id-1:index_id+1]))