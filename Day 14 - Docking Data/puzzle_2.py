#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import itertools

def parse_mem(raw):
    regex = r"mem\[(\d+)\] = (\d+)"
    parsed = re.match(regex, raw, re.MULTILINE).groups()
    return({"adr":int(parsed[0]), "val":int(parsed[1])})

def apply_mask(mask, adr):
    adr = list('{:036b}'.format(adr))
    floating_bits = []
    for i, b in enumerate(list(mask)):
        if b == "1":
            adr[i] = b
        elif b == "X":
            adr[i] = b
            floating_bits.append(i)

    adr_list = []
    for c in itertools.product(["1", "0"], repeat=len(floating_bits)):
        cur_adr = adr.copy()
        for i, b in enumerate(c):
            cur_adr[floating_bits[i]] = b
        
        adr_list.append(int("".join(cur_adr), 2))

    return(adr_list)

# read puzzle input and pad with floor
puzzle_input = []
for l in open("input.txt", "r").read().split("mask = "):
    block = l.strip().split("\n")
    puzzle_input.append({"mask": block[0], "mem_values":[parse_mem(raw) for raw in block[1:]]})

memory = {}
for mask_block in puzzle_input:
    mask = mask_block["mask"]
    for mem_value in mask_block["mem_values"]:
        adr_list = apply_mask(mask, mem_value["adr"])
        print("Writing {} addresses".format(len(adr_list)))
        for adr in adr_list:
            memory[adr] = mem_value["val"]

solution_1 = 0
for adr, val in memory.items():
    solution_1 += val

print(solution_1)