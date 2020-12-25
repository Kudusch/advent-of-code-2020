#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

start_time = datetime.now()

# read puzzle input
puzzle_input = [int(i) for i in list("186524973")]

def insert_in_order(destination, cup_order):
    cup_order = cup_order[0:cup_order.index(destination)+1] + pick_up + cup_order[1+cup_order.index(destination):]
    if not current_cup_label == cup_order[current_cup]:
        shift_value = cup_order.index(current_cup_label) - current_cup
        cup_order = cup_order[shift_value:] + cup_order[0:shift_value]
    return(cup_order)

circumference = len(puzzle_input)
current_cup = 0
cup_order = puzzle_input.copy() + list(range(circumference, 1000000+1))
#cup_order = puzzle_input.copy() + list(range(circumference, 100+1))
circumference = len(cup_order)

round_time = datetime.now()
for move in range(0, 10000000+1):
#for move in range(0, 1000+1):
    final = cup_order.copy()
    current_cup = move % circumference
    current_cup_label = cup_order[current_cup]
    pick_up = []
    for i in range(1, 4):
        pick_up.append(cup_order[(current_cup+i)%circumference])
    
    destination = cup_order[current_cup]-1
    while True:
        if destination not in pick_up and destination != 0:
            break
        else:
            destination = (destination-1)%circumference


    print("\r{:.{}f}".format(move/10000000, 5), end = "")

    #print("cups: {}".format(" ".join([str(i) for i in cup_order])))
    #print("pick up: {}".format(", ".join([str(i) for i in pick_up])))
    #print("destination: {}".format(destination))
    [cup_order.remove(p) for p in pick_up]
    cup_order = insert_in_order(destination, cup_order)

one_index = final.index(1)

print(final[one_index+1])
print(final[one_index+2])