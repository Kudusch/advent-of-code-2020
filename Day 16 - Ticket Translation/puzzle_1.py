#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# read puzzle input
puzzle_input = open("input.txt", "r").read().split("\n\n")
field_ranges = {}
for f in puzzle_input[0].split("\n"):
    parsed_field = re.match(r"(.*): (.*) or (.*)", f)
    field_ranges[parsed_field.groups()[0]] = [parsed_field.groups()[1], parsed_field.groups()[2]]

my_ticket = puzzle_input[1].split("\n")[1].split(",")
nearby_tickets = []
for i, t in enumerate(puzzle_input[2].split("\n")):
    if i > 0:
        nearby_tickets.append([int(i) for i in t.split(",")])

def get_invalid_values(field_ranges):
    valid_values = []
    for key, values in field_ranges.items():
        for value in values:
            valid_values.extend(list(range(int(value.split("-")[0]), int(value.split("-")[1])+1)))
    
    valid_values = sorted(list(set(valid_values)))
    min_valid = min(valid_values)
    max_valid = max(valid_values)
    invalid_values = list(set(range(min_valid, max_valid)) - set(valid_values))
    return({"min":min_valid, "max":max_valid, "invalid":invalid_values})

def get_invalid_field_values(field_ranges):
    valid_values = {}
    for key, values in field_ranges.items():
        valid_values[key] = []
        for value in values:
            valid_values[key].extend(list(range(int(value.split("-")[0]), int(value.split("-")[1])+1)))
    
    return(valid_values)


invalid_values = get_invalid_values(field_ranges)

print("{} tickets found".format(len(nearby_tickets)))
solution_1 = 0
valid_tickets = []
for t in nearby_tickets:
    is_valid = True
    for v in t:
        if v in invalid_values["invalid"]:
            solution_1 += v
            is_valid = False
            break
        elif v < invalid_values["min"]:
            solution_1 += v
            is_valid = False
            break
        elif v > invalid_values["max"]:
            solution_1 += v
            is_valid = False
            break
    if is_valid:
        valid_tickets.append(t)

    
print("Solution to part 1: {}".format(solution_1))

invalid_field_values = get_invalid_field_values(field_ranges)

print("After first check, there are {} tickets left".format(len(valid_tickets)))

field_positions = [[]]*len(field_ranges.keys())
for t in valid_tickets:
    for i, value in enumerate(t):
        field_positions[i] = field_positions[i] + [value]

field_names = [k for k in field_ranges.keys()]

solved_fields = [[]]*len(field_ranges.keys())
for i, f in enumerate(field_positions):
    for field_name in field_names:
        if (False not in [v in invalid_field_values[field_name] for v in f]):
            solved_fields[i] = solved_fields[i] + [field_name]

solution_2 = [[]]*len(field_ranges.keys())
for i, s in enumerate(solved_fields):
    solution_2[len(s)-1] = [i,s]

solved_fields = {}
for s in solution_2:
    for solved_field in [k for k in solved_fields.keys()]:
        s[1].remove(solved_field)
    solved_fields[s[1][0]] = s[0]

departure_fields = []
for s in solved_fields.items():
    print(s[0], s[1])
    if "departure" == s[0].split(" ")[0]:
        departure_fields.append(s[1])

solution_2 = 1
for f in departure_fields:
    print(my_ticket[f])
    solution_2 = solution_2 * int(my_ticket[f])

print(solution_2)