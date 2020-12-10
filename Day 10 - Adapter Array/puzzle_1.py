#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

def is_chain_valid(adapter_chain):
    for i in range(0, len(adapter_chain)-1):
        jolt_delta = adapter_chain[i+1]-adapter_chain[i]
        if jolt_delta > 3:
            return False
    return True

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append(int(l))

puzzle_input.sort()

adapter_chain = puzzle_input.copy()

adapter_chain.append(adapter_chain[-1:][0] + 3)
adapter_chain = [0] + adapter_chain

jolt_deltas = []
for i in range(0, len(adapter_chain)-1):
    jolt_deltas.append(adapter_chain[i+1]-adapter_chain[i])

print("There are {} 1-jolt-differences".format(jolt_deltas.count(1)))
print("There are {} 3-jolt-differences".format(jolt_deltas.count(3)))

print("\t-> Solution to part 1 is: {}\n".format(jolt_deltas.count(1) * jolt_deltas.count(3)))

# is_chain_valid(adapter_chain)
# print("adapter\tdelta")
# for i in range(1, len(adapter_chain)):
#    print("{}\t{}".format(adapter_chain[i], jolt_deltas[i-1]))


skippable_adapters = []
skippable_adapters_count = 0
for i in range(1, len(adapter_chain)-1):
    if (adapter_chain[i+1]-adapter_chain[i-1]) <= 3:
        skippable_adapters.append(adapter_chain[i])
        skippable_adapters_count += 1

possible_combinations_window = []
for i in range(1, len(adapter_chain)-1):
    if adapter_chain[i] in skippable_adapters:
        possible_combinations_window.append("1")
    else:
        possible_combinations_window.append("0")

m = 0
n = 0
for l in "".join(possible_combinations_window).split("0"):
    if len(l) > 0:
        if len(l) == 3:
            m += 1
        else:
            n += len(l)

possible_combinations = (((2**3)-1)**m)*(2**n)
print("There are {} possible combinations".format(possible_combinations))