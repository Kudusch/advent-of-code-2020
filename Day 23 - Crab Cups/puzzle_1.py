#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

start_time = datetime.now()

# read puzzle input
puzzle_input = [int(i) for i in list("186524973")]
puzzle_input = [int(i) for i in list("389125467")]

def insert_in_order(destination, cup_order):
    cup_order = cup_order[0:cup_order.index(destination)+1] + pick_up + cup_order[1+cup_order.index(destination):]
    if not current_cup_label == cup_order[current_cup]:
        shift_value = cup_order.index(current_cup_label) - current_cup
        cup_order = cup_order[shift_value:] + cup_order[0:shift_value]
    return(cup_order)

circumference = len(puzzle_input)
current_cup = 0
cup_order = puzzle_input.copy()

for move in range(0, 101):
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


    print("-- move {} --".format(move+1))
    print("cups: {}".format(" ".join([str(i) for i in cup_order])))
    print("pick up: {}".format(", ".join([str(i) for i in pick_up])))
    print("destination: {}".format(destination))
    [cup_order.remove(p) for p in pick_up]
    cup_order = insert_in_order(destination, cup_order)
    #print("")

while True:
    if final[0] == 1:
        break
    shift = final.pop()
    final = [shift] + final

print("Solved in {}".format(datetime.now()-start_time))
if "45983627" == "".join([str(i) for i in final[1:]]):
    print("Test ok")
else:
    print("Test not ok")