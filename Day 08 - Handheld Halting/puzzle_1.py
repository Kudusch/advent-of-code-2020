#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    operation = l.split()
    operation[1] = int(operation[1])
    puzzle_input.append(operation)


def switch_operation(operation):
    if (operation[0] == "jmp"):
        return(["nop", operation[1]])
    elif (operation[0] == "nop"):
        return(["jmp", operation[1]])
    else:
        return(operation)


def run_boot_code(boot_code):
    visited_indices = []
    cur_index = 0
    loop_detection = False
    accumulator = 0
    while not loop_detection:
        if cur_index in visited_indices:
            print("Terminated at loop with the accumulator at: {}".format(accumulator))
            visited_indices.append(cur_index)
            return(visited_indices)
            loop_detection = True
        else:
            cur_operation = boot_code[cur_index]
            visited_indices.append(cur_index)
            if cur_operation[0] == "acc":
                accumulator += cur_operation[1]
                cur_index += 1
            elif cur_operation[0] == "jmp":
                cur_index += cur_operation[1]
            elif cur_operation[0] == "nop":
                cur_index += 1

            if cur_index >= len(boot_code):
                print("Terminated at end with the accumulator at: {}".format(accumulator))
                loop_detection = True
                return(True)

def analyze_boot_code(boot_code):
    visited_indices = run_boot_code(boot_code)
    for operation in visited_indices:
        if boot_code[operation][0] in ["jmp", "nop"]:
            boot_code_mod = boot_code.copy()
            boot_code_mod[operation] = switch_operation(boot_code_mod[operation])
            return_boot_code = run_boot_code(boot_code_mod)
            if return_boot_code is True:
                return(return_boot_code)


analyze_boot_code(puzzle_input)