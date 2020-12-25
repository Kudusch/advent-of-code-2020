#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

neighbor_directions = ["e", "se", "sw", "w", "nw", "ne"]

# read puzzle input
puzzle_input = []
for l in open("input.txt", "r").readlines():
    regex = r"(e|se|sw|w|nw|ne)"
    matches = re.finditer(regex, l, re.MULTILINE)
    puzzle_input.append([neighbor_directions.index(match.group()) for match in matches])

def move_tile(d, coord):
    if neighbor_directions[d] == "e":
        coord["x"] += 1
        coord["y"] -= 1
    elif neighbor_directions[d] == "w":
        coord["x"] -= 1
        coord["y"] += 1
    elif neighbor_directions[d] == "se":
        coord["y"] -= 1
        coord["z"] += 1
    elif neighbor_directions[d] == "sw":
        coord["x"] -= 1
        coord["z"] += 1
    elif neighbor_directions[d] == "ne":
        coord["x"] += 1
        coord["z"] -= 1
    elif neighbor_directions[d] == "nw":
        coord["y"] += 1
        coord["z"] -= 1
    return(coord)

def get_neighbors(coord):
    x = coord["x"]
    y = coord["y"]
    z = coord["z"]
    active_neighbors = []
    possible_neighbors = [
        {"x":x, "y":y-1, "z":z+1},
        {"x":x, "y":y+1, "z":z-1},
        {"x":x+1, "y":y, "z":z-1},
        {"x":x-1, "y":y, "z":z+1},
        {"x":x+1, "y":y-1, "z":z},
        {"x":x-1, "y":y+1, "z":z}
    ]
    return(possible_neighbors)

def get_flipped_neighbors(coord, tile_map):
    possible_neighbors = get_neighbors(coord)
    return([p in tile_map for p in possible_neighbors].count(True), possible_neighbors)

def get_ranges():
    ranges = {}
    z = []
    y = []
    x = []
    for coord in tile_map:
        z.append(coord["z"])
        y.append(coord["y"])
        x.append(coord["x"])
    ranges["z_min"] = min(z)-1
    ranges["z_max"] = max(z)+1
    ranges["y_min"] = min(y)-1
    ranges["y_max"] = max(y)+1
    ranges["x_min"] = min(x)-1
    ranges["x_max"] = max(x)+1
    return(ranges)

def remove_duplicates(l):
    seen = set()
    new_l = []
    for d in l:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            new_l.append(d)
    return(new_l)


tiles_flipped = []
for tile in puzzle_input:
    current_coord = {"x":0, "y":0, "z":0}
    for d in tile:
        current_coord = move_tile(d, current_coord)
    if (current_coord in tiles_flipped):
        tiles_flipped.remove(current_coord)
    else:
        tiles_flipped.append(current_coord)

print("There are {} black tiles".format(len(tiles_flipped)))

tile_map = [s.copy() for s in tiles_flipped]

# for t in tiles_flipped:
#     print(t, get_flipped_neighbors(t))

max_cycles = 100
for current_cycle in range(0, max_cycles):
    new_tile_map = tile_map.copy()
    all_neighboring_tiles = []
    for tile in tile_map:
        neighboring_tiles = get_flipped_neighbors(tile, tile_map)
        all_neighboring_tiles.extend(neighboring_tiles[1])
        if neighboring_tiles[0] == 0 or neighboring_tiles[0] > 2:
            new_tile_map.remove(tile)
    for coord in all_neighboring_tiles:
        if all_neighboring_tiles.count(coord) == 2:
            if coord not in new_tile_map:
                new_tile_map.append(coord)

    print("Day {} ({} flipped tiles)".format(current_cycle+1, len(new_tile_map)))
    tile_map = new_tile_map.copy()

print("\nThere are {} flipped tiles".format(len(new_tile_map)))
