#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input

puzzle_input = open("input.txt", "r").read().split("\n\n")
rules = {}
for rule in puzzle_input[0].split("\n"):
    key, rule = rule.strip().split(": ")
    rule_list = []
    if not "\"" in rule:
        for i, alt_rule in enumerate(rule.split(" | ")):
            alt_rule_list = []
            for sub_rule in alt_rule.split(" "):
                alt_rule_list.append(int(sub_rule))
            rule_list.append(alt_rule_list)
    else:
        rule_list = rule
    rules[int(key)] = rule_list

messages = []
for message in puzzle_input[1].split("\n"):
    messages.append(message.strip())
max_len = max([len(m) for m in messages])

def test(s, seq):
    if s == '' or seq == []: return s == '' and seq == []
    r = rules[seq[0]]
    if '"' in r:
        return test(s[1:], seq[1:]) if s[0] in r else False
    else:
        return any(test(s, t + seq[1:]) for t in r)

print("Part 1:", sum(test(m,[0]) for m in messages))

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

print("Part 2:", sum(test(m,[0]) for m in messages))