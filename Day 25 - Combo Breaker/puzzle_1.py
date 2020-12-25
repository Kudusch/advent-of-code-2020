#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input
public_keys = [7573546, 17786549]
#public_keys = [17807724, 5764801]

initial_subject = 7

def brute_force(key):
    current_loop = 1
    solved_key = 1
    while solved_key != key:
        solved_key = (solved_key * initial_subject) % 20201227
        current_loop += 1
    return(current_loop-1)

loop_sizes = [brute_force(public_keys[0]), brute_force(public_keys[1])]

print("To get {} use loop size: {}".format(
    public_keys[0], loop_sizes[0])
)
print("To get {} use loop size: {}".format(
    public_keys[1], loop_sizes[1])
)

solved_keys = [1, 1]
for i in range(loop_sizes[0]):
    solved_keys[0] = (solved_keys[0] * public_keys[1]) % 20201227
for i in range(loop_sizes[1]):
    solved_keys[1] = (solved_keys[1] * public_keys[0]) % 20201227

if len(set(solved_keys)) == 1:
    print("The encryption key is {}".format(solved_keys[0]))
