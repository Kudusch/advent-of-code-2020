#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input to list of integers
puzzle_input = open("input.txt", "r").read().split("\n\n")

custom_groups = []
for group in puzzle_input:
    custom_groups.append([person.strip() for person in group.split("\n")])

n_questions_anyone = 0
for group in custom_groups:
    n_questions_anyone += len(set("".join(group)))

print("A total of {} questions were answered by anyone in a group.".format(n_questions_anyone))

n_questions_everyone = 0
for group in custom_groups:
    group_size = len(group)
    n_group_question = 0
    for q in set("".join(group)):
        if (False not in [q in g for g in group]):
            n_group_question += 1

    n_questions_everyone += n_group_question

print("A total of {} questions were answered by everyone in a group.".format(n_questions_everyone))