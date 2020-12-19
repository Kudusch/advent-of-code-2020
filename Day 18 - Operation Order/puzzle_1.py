#!/usr/bin/env python
# -*- coding: utf-8 -*-}

import re

# read puzzle input
puzzle_input = []
for l in open("input.txt", "r").readlines():
    puzzle_input.append("(" + l.strip() + ")")

def solve_simple(simple_expression):
    simple_expression = [i for i in simple_expression.split(" ") if i != ""] 
    simple_expression = ["*", "1", "*"] + simple_expression
    solution = 1
    for i in range(1, len(simple_expression), 2):
        solution = eval("{}{}{}".format(solution, simple_expression[i-1], simple_expression[i]))
    return(solution)

def solve_simple_adv(simple_expression):
    simple_expression = re.sub(r"(\d+\s*\+\s*[+\d ]+)", " ( \\1 ) ", simple_expression, 0)
    simple_expression = [i for i in simple_expression.split(" ") if i != ""] 
    simple_expression = " ".join(simple_expression)
    solution = eval(simple_expression)
    return(solution)

def solve_expression(raw_expr, mode):
    if "(" in raw_expr:
        pars = re.finditer(r"\([ \-\+*0-9]+\)", raw_expr)
        par_solutions = []
        for par in pars:
            par_solution = solve_expression(par.group()[1:-1], mode)
            par_solutions.append([par.start(), par.end(), str(par_solution)])
        new_expr = list(raw_expr)
        for s in par_solutions:
            new_expr[s[0]:s[1]] = s[2] + " "*((s[1]-s[0])-len(s[2]))
        new_expr = "".join(new_expr)
        solution = solve_expression(new_expr, mode)
    else:
        if mode == "adv":
            solution = solve_simple_adv(raw_expr)
        elif mode == "normal":
            solution = solve_simple(raw_expr)
    
    return(solution)

solution_1 = 0
solution_2 = 0
for expr in puzzle_input:
    normal = solve_expression(expr, "normal")
    advanced = solve_expression(expr, "adv")
    expr = "".join([i for i in list(expr) if i != " "])
    print("{} = {} (adv: {})".format(expr, normal, advanced))
    solution_1 += normal
    solution_2 += advanced

print("\tSolution to part 1: {}".format(solution_1))
print("\tSolution to part 2: {}".format(solution_2))

