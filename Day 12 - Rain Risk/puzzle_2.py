#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input and pad with floor
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append([l[0], int(l[1:].strip())])

def change_direction(direction, degrees, waypoint):
    new_waypoint = {"v":0, "h":0}
    if degrees == 180:
        new_waypoint["h"] = waypoint["h"]*-1
        new_waypoint["v"] = waypoint["v"]*-1
        return(new_waypoint)
    
    if degrees == 270:
        direction = "L" if direction == "R" else "R"
    
    if direction == "R":
        new_waypoint["h"] = waypoint["v"]
        new_waypoint["v"] = waypoint["h"]*-1
    elif direction == "L":
        new_waypoint["v"] = waypoint["h"]
        new_waypoint["h"] = waypoint["v"]*-1

    return(new_waypoint)

print(change_direction("R", 90, {"h":10, "v":-18}))

manhattan_distance = {"v":0, "h":0}
waypoint = {"v":1, "h":10}
# 0:E, 1:S, 2:W, 3:N
#print(waypoint)
#print(manhattan_distance)
#print("")

for c in puzzle_input:
    #print(c)
    current_command = c[0]
    delta = c[1]
    
    if current_command == "F":
        manhattan_distance["v"] = manhattan_distance["v"] + (waypoint["v"]*delta)
        manhattan_distance["h"] = manhattan_distance["h"] + (waypoint["h"]*delta)
    
    #print(current_command, delta)
    
    if current_command == "N":
        waypoint["v"] = waypoint["v"] + delta
    elif current_command == "S":
        waypoint["v"] = waypoint["v"] - delta
    elif current_command == "W":
        waypoint["h"] = waypoint["h"] - delta
    elif current_command == "E":
        waypoint["h"] = waypoint["h"] + delta
    
    if current_command in ["L", "R"]:
        waypoint = change_direction(current_command, delta, waypoint)
    
    #print(waypoint)
    #print(manhattan_distance)
    #print("")
    
print(sum([abs(n[1]) for n in manhattan_distance.items()]))
