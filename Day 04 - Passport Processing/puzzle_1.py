#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

key_list = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

def parse_passport(passport):
    passport = [p.split(":") for p in passport.split()]
    passport_dict = {}
    for entry in passport:
        passport_dict[entry[0]] = entry[1]
    return(passport_dict)

def is_byr_valid(value):
    try:
        value = int(value)
        if value >= 1920 and value <= 2002:
            return True
        else:
            return False    
    except:
        return False

def is_iyr_valid(value):
    try:
        value = int(value)
        if value >= 2010 and value <= 2020:
            return True
        else:
            return False    
    except:
        return False

def is_eyr_valid(value):
    try:
        value = int(value)
        if value >= 2020 and value <= 2030:
            return True
        else:
            return False    
    except:
        return False

def is_hgt_valid(value):
    if value[-2:] == "cm":
        try:
            if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                return True
            else:
                return False    
        except:
            return False
    elif value[-2:] == "in":
        try:
            if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                return True
            else:
                return False    
        except:
            return False
    else:
        return False

def is_hcl_valid(value):
    if re.match(r"#[0-9abcdef]{6}", value):
        return True
    else:
        return False

def is_ecl_valid(value):
    if value in "amb blu brn gry grn hzl oth".split():
        return True
    else:
        return False

def is_pid_valid(value):
    if re.match(r"^\d{9}$", value):
        return True
    else:
        return False


def validate_passport(passport):
    try:
        byr_valid = is_byr_valid(passport["byr"])
    except:
        byr_valid = False
    
    try:
        iyr_valid = is_iyr_valid(passport["iyr"])
    except:
        iyr_valid = False
    
    try:
        eyr_valid = is_eyr_valid(passport["eyr"])
    except:
        eyr_valid = False
    
    try:
        hgt_valid = is_hgt_valid(passport["hgt"])
    except:
        hgt_valid = False
    
    try:
        hcl_valid = is_hcl_valid(passport["hcl"])
    except:
        hcl_valid = False
    
    try:
        ecl_valid = is_ecl_valid(passport["ecl"])
    except:
        ecl_valid = False
    
    try:
        pid_valid = is_pid_valid(passport["pid"])
    except:
        pid_valid = False

    return (byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid)
    # print("byr_valid", byr_valid)
    # print("iyr_valid", iyr_valid)
    # print("eyr_valid", eyr_valid)
    # print("hgt_valid", hgt_valid)
    # print("hcl_valid", hcl_valid)
    # print("ecl_valid", ecl_valid)
    # print("pid_valid", pid_valid)
    



# read puzzle input to list of integers
puzzle_input = []
for l in open("input.txt", "r").read().split("\n\n"):
    puzzle_input.append(parse_passport(l)) 


print("{} passports found".format(len(puzzle_input)))

solution_one = 0
solution_two = []
for p in puzzle_input:
    if (sum([k in p.keys() for k in key_list]) == 7):
        solution_one += 1
    solution_two.append(validate_passport(p))


print("{} have all (relevant) keys".format(solution_one))

print("{} are valid".format(sum(solution_two)))