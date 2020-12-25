#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

# read puzzle input
puzzle_input = {}
for l in open("input_test.txt", "r").read().split("\n\n"):
    tid, tile = l.split(":")
    puzzle_input[int(tid[4:])] = [t for t in list(tile) if not t == "\n"]

#   0
#  ###
# 3###1
#  ###
#   2
# l->r, t->b
dim = int(math.sqrt(len(puzzle_input)))
tile_edges = {}
for tid, tile in puzzle_input.items():
    tile_edges[tid] = [tile[0:10], tile[9:101:10], list(reversed(tile[-10:])), list(reversed(tile[0:91:10]))]

all_edges = []
for tid, edges in tile_edges.items():
    all_edges.extend(edges)
    all_edges.extend([list(reversed(edge)) for edge in edges])

border_edges = []
for edge in all_edges:
    if all_edges.count(edge) == 1:
        border_edges.append(edge)

border_tiles = []
corner_tiles = []
for tid, edges in tile_edges.items():
    n = 0
    for edge in edges:
        if edge in border_edges or list(reversed(edge)) in border_edges:
            n +=1
    if n == 2:
        corner_tiles.append(tid)
    elif n == 1:
        border_tiles.append(tid)

border_tiles = list(set(border_tiles))
corner_tiles = list(set(corner_tiles))
frame_tiles = border_tiles + corner_tiles
solution_1 = 1
for tid in corner_tiles:
    solution_1 = solution_1 * tid
print("The solution to part 1 is {}".format(solution_1))