#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input and pad with floor
puzzle_input = []
dimensions = {}
for l in open("input.txt", "r").readlines():
    puzzle_input.append(["."] + list(l.strip()) + ["."])
    dimensions["x"] = len(list(l.strip()))

dimensions["y"] = len(puzzle_input)

puzzle_input.append(list("."*(dimensions["x"]+2)))
puzzle_input = [list("."*(dimensions["x"]+2))] + puzzle_input

# If empty and there are no occupied seats adjacent to it, change
# If occupied and >=4 seats adjacent to it are also occupied, change

# 0 1 2
# 3 . 4
# 5 6 7

def get_occupied_seats(y, x, seat_map):
    occupied_seats = {}
    if (seat_map[y-1][x-1] == "#"):
        occupied_seats[0] = [y-1, x-1]
    
    if (seat_map[y-1][x] == "#"):
        occupied_seats[1] = [y-1, x]
    
    if (seat_map[y-1][x+1] == "#"):
        occupied_seats[2] = [y-1, x+1]
    
    if (seat_map[y][x-1] == "#"):
        occupied_seats[3] = [y, x-1]
    
    if (seat_map[y][x+1] == "#"):
        occupied_seats[4] = [y, x+1]
    
    if (seat_map[y+1][x-1] == "#"):
        occupied_seats[5] = [y+1, x-1]
    
    if (seat_map[y+1][x] == "#"):
        occupied_seats[6] = [y+1, x]
    
    if (seat_map[y+1][x+1] == "#"):
        occupied_seats[7] = [y+1, x+1]
    
    return(occupied_seats)


seat_map = [s.copy() for s in puzzle_input]
change_detected = True
change_cycles = 0
while change_detected:
    seat_map_changed = [s.copy() for s in seat_map]
    change_detected = False
    print("Cycle {} ----------".format(change_cycles))
    for y in range(1, len(puzzle_input)-1):
        print("")
        for x in range(1, len(puzzle_input[y])-1):
            occupied_seats = get_occupied_seats(y, x, seat_map)
            print(seat_map[y][x], end="")
            #print(len(occupied_seats), end="")
            if seat_map[y][x] == "L":
                if len(occupied_seats) == 0:
                    seat_map_changed[y][x] = "#"
                    change_detected = True
            elif seat_map[y][x] == "#":
                if len(occupied_seats) >= 4:
                    seat_map_changed[y][x] = "L"
                    change_detected = True
    change_cycles += 1
    seat_map = seat_map_changed.copy()
    print("\n-------------------\n".format(change_cycles))


occupied_seats = 0
for y in range(1, len(puzzle_input)-1):
    for x in range(1, len(puzzle_input[y])-1):
        if seat_map[y][x] == "#":
            occupied_seats += 1


print("There are {} occupied seats after {} cycles.".format(occupied_seats, change_cycles))