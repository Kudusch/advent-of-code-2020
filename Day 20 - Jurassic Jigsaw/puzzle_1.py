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

def print_tile(tile, rot, flip):
    print_tile = []
    
    if rot == 3:
        for i in range(0, int(math.sqrt(len(tile)))):
            start = 0+(i*int(math.sqrt(len(tile))))
            stop = 10+start
            print_tile.append(list(reversed(tile[start:stop])))
    elif rot == 1:
        for i in range(0, int(math.sqrt(len(tile)))):
            start = 9-i
            stop = 100
            print_tile.append(list(reversed(tile[start:stop:10])))
        flip = not flip
    else:
        for i in range(0, int(math.sqrt(len(tile)))):
            start = 0+(i*int(math.sqrt(len(tile))))
            stop = 10+start
            print_tile.append(tile[start:stop])
    if flip:
        print_tile = list(reversed(print_tile))
    
    # for y in print_tile:
    #     for x in y:
    #         print(x, end="")
    #     print()
    # print("")
    return(print_tile)




image_map = [[(corner_tiles[0], 0, False)]]
used_tiles = [corner_tiles[0]]

y_edge = 
x_edge = 
for y in range(0, dim):
    for x in range(0, dim-1):
        current_tile = image_map[y][-1][0]
        current_edges = tile_edges[current_tile]
        for j, current_edge in enumerate(current_edges):
            if j % 2 == 1:
                for tid, tile_edge in tile_edges.items():
                    if not tid in used_tiles:
                        for i, e in enumerate(tile_edge):
                            if current_edge == e:
                                print(j,i,tid)
                                used_tiles[y].append((tid,))
                            elif current_edge == reversed(e):
                                print(j,i,tid)

    
    #print(image_map)

image_map = image_map[0:-1]
print(image_map)

# final_image = []
# for i, r in enumerate(image_map):
#     for j, c in enumerate(r):
#         t = print_tile(puzzle_input[c[0]], c[1], c[2])
#         final_image.append(t)

# assembled_image = [[]]*(10*dim)
# n = 0
# for i in range(0, dim):
#     for j in range(0, 10):
#         assembled_image[n] = list(reversed(final_image[i][j])) + list(reversed(final_image[i+3][j])) + list(reversed(final_image[i+6][j]))
#         print("".join(assembled_image[n]))
#         n += 1

# print(len(assembled_image))