#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").readlines():
    parts = l.split(":")
    req = parts[0].strip().split(" ")
    password = parts[1].strip()
    puzzle_input.append([req, password])

def check_password_one(password, req):
    min_n = int(req[0].split("-")[0])
    max_n = int(req[0].split("-")[1])
    n = password.count(req[1])
    if n <= max_n and n >= min_n:
        return 1
    else:
        return 0

def check_password_two(password, req):
    pos = [int(p) for p in req[0].split("-")]
    if (password[pos[0]-1] == req[1]) ^ (password[pos[1]-1] == req[1]):
        return 1
    else:
        return 0
    

solution_one = 0
solution_two = 0
for pw in puzzle_input:
    solution_one += check_password_one(pw[1], pw[0])
    solution_two += check_password_two(pw[1], pw[0])


print(solution_two)