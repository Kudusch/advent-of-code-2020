#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input and pad with floor
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append([l[0], int(l[1:].strip())])

def change_direction(direction, degrees, facing_direction):
    if (direction == "L"):
        return(int((facing_direction - (degrees / 90)) % 4))
    elif (direction == "R"):
        return(int((facing_direction + (degrees / 90)) % 4))
        

manhattan_distance = {"v":0, "h":0}
# 0:E, 1:S, 2:W, 3:Na

facing_direction = 0
facing_direction_names = ["E", "S", "W", "N"]

for c in puzzle_input:
    #print(c)

    current_command = c[0]
    delta = c[1]
    if current_command == "F":
        current_command = facing_direction_names[facing_direction]
    
    #print(current_command, delta)
    
    if current_command == "N":
        manhattan_distance["v"] = manhattan_distance["v"] + delta
    elif current_command == "S":
        manhattan_distance["v"] = manhattan_distance["v"] - delta
    elif current_command == "W":
        manhattan_distance["h"] = manhattan_distance["h"] + delta
    elif current_command == "E":
        manhattan_distance["h"] = manhattan_distance["h"] - delta
    
    if current_command in ["L", "R"]:
        facing_direction = change_direction(current_command, delta, facing_direction)
    
print(sum([abs(n[1]) for n in manhattan_distance.items()]))



