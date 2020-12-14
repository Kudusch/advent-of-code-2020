#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def parse_mem(raw):
    regex = r"mem\[(\d+)\] = (\d+)"
    parsed = re.match(regex, raw, re.MULTILINE).groups()
    return({"adr":int(parsed[0]), "val":int(parsed[1])})

def apply_mask(mask, value):
    value = list('{:036b}'.format(value))
    for i, b in enumerate(list(mask)):
        if not b == "X":
            value[i] = b
    return(int("".join(value), 2))

# read puzzle input and pad with floor
puzzle_input = []
for l in open("input.txt", "r").read().split("mask = "):
    block = l.strip().split("\n")
    puzzle_input.append({"mask": block[0], "mem_values":[parse_mem(raw) for raw in block[1:]]})

memory = {}
for mask_block in puzzle_input:
    mask = mask_block["mask"]
    for mem_value in mask_block["mem_values"]:
        memory[mem_value["adr"]] = apply_mask(mask, mem_value["val"])

solution_1 = 0
for adr, val in memory.items():
    solution_1 += val

print(solution_1)