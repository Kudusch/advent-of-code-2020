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

def get_first_seat(y, x, hor, ver, seat_map):
    seat_found = False
    distance = 1
    while not seat_found:
        try:
            if (y+(distance*ver) >= 0) and x+(distance*hor) >= 0:
                if (seat_map[y+(distance*ver)][x+(distance*hor)] == "#"):
                    return([y+(distance*ver), x+(distance*hor)])
                    seat_found = True
                elif (seat_map[y+(distance*ver)][x+(distance*hor)] == "L"):
                    seat_found = True
            else:
                return(None)
        except:
            return(None)
        
        distance += 1

def get_occupied_seats(y, x, seat_map):
    occupied_seats = {}
    occupied_seats[0] = get_first_seat(
        y = y, 
        x = x, 
        hor = -1, 
        ver = -1, 
        seat_map = seat_map
    )

    occupied_seats[1] = get_first_seat(
        y = y, 
        x = x, 
        hor = 0, 
        ver = -1, 
        seat_map = seat_map
    )

    occupied_seats[2] = get_first_seat(
        y = y, 
        x = x, 
        hor = 1, 
        ver = -1, 
        seat_map = seat_map
    )
    occupied_seats[3] = get_first_seat(
        y = y, 
        x = x, 
        hor = -1, 
        ver = 0, 
        seat_map = seat_map
    )

    occupied_seats[4] = get_first_seat(
        y = y, 
        x = x, 
        hor = 1, 
        ver = 0, 
        seat_map = seat_map
    )

    occupied_seats[5] = get_first_seat(
        y = y, 
        x = x, 
        hor = -1, 
        ver = 1, 
        seat_map = seat_map
    )

    occupied_seats[6] = get_first_seat(
        y = y, 
        x = x, 
        hor = 0, 
        ver = 1, 
        seat_map = seat_map
    )

    occupied_seats[7] = get_first_seat(
        y = y, 
        x = x, 
        hor = 1, 
        ver = 1, 
        seat_map = seat_map
    )
    returned_seats = 0
    for seat in occupied_seats.items():
        if seat[1]:
            returned_seats += 1
    return(returned_seats)


seat_map = [s.copy() for s in puzzle_input]
change_detected = True
change_cycles = 0
while change_detected:
    seat_map_changed = [s.copy() for s in seat_map]
    change_detected = False
    #print("Cycle {} ----------".format(change_cycles))
    for y in range(1, len(puzzle_input)-1):
        #print("")
        for x in range(1, len(puzzle_input[y])-1):
            occupied_seats = get_occupied_seats(y, x, seat_map)
            #print(seat_map[y][x], end="")
            #print(occupied_seats, end="")
            if seat_map[y][x] == "L":
                if occupied_seats == 0:
                    seat_map_changed[y][x] = "#"
                    change_detected = True
            elif seat_map[y][x] == "#":
                if occupied_seats >= 5:
                    seat_map_changed[y][x] = "L"
                    change_detected = True
    change_cycles += 1
    seat_map = seat_map_changed.copy()
    #print("\n-------------------\n".format(change_cycles))


occupied_seats = 0
for y in range(1, len(puzzle_input)-1):
    for x in range(1, len(puzzle_input[y])-1):
        if seat_map[y][x] == "#":
            occupied_seats += 1


print("There are {} occupied seats after {} cycles.".format(occupied_seats, change_cycles))