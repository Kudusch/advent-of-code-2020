#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

# read puzzle input
# active cubes as coords: z, y, x
puzzle_input = []
for i, l in enumerate(open("input_test.txt", "r").readlines()):
    for j, cube in enumerate(list(l.strip())):
        if cube == "#":
            puzzle_input.append([0, i, j])

reactor_map = [s.copy() for s in puzzle_input]

def get_active_neighbors(z, y, x):
    neighbors = []
    possible_neighbors = [[z-1, z, z+1],[y-1, y, y+1],[x-1, x, x+1]]
    possible_neighbors = [list(n) for n in itertools.product(*possible_neighbors)]
    possible_neighbors.remove([z, y, x])
    return([p in reactor_map for p in possible_neighbors].count(True))

def get_ranges():
    ranges = {}
    z = [p[0] for p in reactor_map]
    y = [p[1] for p in reactor_map]
    x = [p[2] for p in reactor_map]
    ranges["z_min"] = min(z)-1
    ranges["z_max"] = max(z)+1
    ranges["y_min"] = min(y)-1
    ranges["y_max"] = max(y)+1
    ranges["x_min"] = min(x)-1
    ranges["x_max"] = max(x)+1
    return(ranges)

[print(p) for p in reactor_map]
print(get_active_neighbors(0, 0, 1))

max_cycles = 6
for current_cycle in range(1, max_cycles+1):
    new_reactor_map = [s.copy() for s in reactor_map]
    ranges = get_ranges()
    print("Cycle {}".format(current_cycle))
    for z in range(ranges["z_min"], ranges["z_max"]+1):
        for y in range(ranges["y_min"], ranges["y_max"]+1):
            for x in range(ranges["x_min"], ranges["x_max"]+1):
                active_neighbors = get_active_neighbors(z,y,x)
                if [z,y,x] in reactor_map:
                    if active_neighbors < 2 or active_neighbors > 3:
                        new_reactor_map.remove([z,y,x])
                        print("{},{},{}\t({} active neighbors)\tremoved".format(z, y, x, active_neighbors))
                else:
                    if active_neighbors == 3:
                        new_reactor_map.append([z,y,x])
                        print("{},{},{}\t({} active neighbors)\tadded".format(z, y, x, active_neighbors))

    reactor_map = [s.copy() for s in new_reactor_map]

print("\nThere are {} active cubes".format(len(new_reactor_map)))