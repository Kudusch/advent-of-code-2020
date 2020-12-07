#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import igraph
from igraph import *
import math
from itertools import repeat

# read puzzle input to list of integers
puzzle_input = {}
for l in open("input.txt", "r").readlines():
    l = l.strip().split(" bags contain ")
    bag_color = l[0]
    if (l[1] != "no other bags."):
        rules = [re.search(r"(\d+)\s(.*?)\sbags?", rule).groups() for rule in l[1].split(", ")]
    else:
        rules = None

    puzzle_input[bag_color] = rules

all_bags = []
for bag, rules in puzzle_input.items():
    if rules:
        possible_bags = [rule[1] for rule in rules]
    all_bags.append(bag)
    all_bags.extend(possible_bags)

all_bags = set(all_bags)

puzzle_graph_edges = {}
for bag, rules in puzzle_input.items():
    if rules:
        puzzle_graph_edges[bag] = [rule[1] for rule in rules]

puzzle_graph = igraph.Graph(directed=True)
puzzle_vertices = list(set(list(puzzle_graph_edges.keys()) + list([a for v in puzzle_graph_edges.values() for a in v])))
puzzle_graph.add_vertices(puzzle_vertices)
puzzle_graph.add_edges([(v, a) for v in puzzle_graph_edges.keys() for a in puzzle_graph_edges[v]])


solution = 0
for bag in all_bags:
    path = puzzle_graph.shortest_paths_dijkstra(source=bag, target="shiny gold", mode=OUT)[0][0]
    if not math.isinf(path) and path > 0:
        solution += 1

print(solution)

solution = 0
def get_all_bags(bag):
    global solution
    solution += sum([int(b[0]) for b in puzzle_input[bag]])
    bags_to_check = [list(repeat(b[1], int(b[0]))) for b in puzzle_input[bag]]
    bags_to_check = [item for sublist in bags_to_check for item in sublist]
    for b in bags_to_check:
        if (puzzle_input[b]):
            get_all_bags(b)

get_all_bags("shiny gold")

print(solution)