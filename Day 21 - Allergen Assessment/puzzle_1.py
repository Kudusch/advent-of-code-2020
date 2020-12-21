#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input
puzzle_input = []
all_allergens = []
all_ingredients = []
for l in open("input_test.txt", "r").readlines():
    ingredients, allergens = l.split(" (contains ")
    ingredients = ingredients.split(" ")
    all_ingredients.extend(ingredients)
    allergens = allergens.strip()
    allergens = allergens[:-1].split(", ")
    all_allergens.extend(allergens)
    puzzle_input.append([ingredients, allergens])

all_allergens = set(all_allergens)
all_ingredients = set(all_ingredients)

ingredients_dict = {}
for ingredient in all_ingredients:
    ingredients_dict[ingredient] = []
    for food in puzzle_input:
        if ingredient in food[0]:
            ingredients_dict[ingredient].extend(food[1])

allergens_dict = {}
for allergen in all_allergens:
    allergens_dict[allergen] = []
    for food in puzzle_input:
        if allergen in food[1]:
            allergens_dict[allergen].append(food[0])

no_allergens = {}
for ingredient in all_ingredients:
    no_allergens[ingredient] = []
    for allergen in ingredients_dict[ingredient]:
        no_allergens[ingredient].append(any([ingredient not in allergen_list for allergen_list in allergens_dict[allergen]]))
no_allergens = [i for i, b in no_allergens.items() if False not in b]

solution_1 = 0
for food in puzzle_input:
    solution_1 += sum([food[0].count(allergen) for allergen in no_allergens])

print("The solution to part 1 is: {}".format(solution_1))

food_list = puzzle_input.copy()
for food in food_list:
    [food[0].remove(a) for a in no_allergens if a in food[0]]

[all_ingredients.remove(a) for a in no_allergens]
[ingredients_dict.pop(a) for a in no_allergens]

solution_2 = {}
for i in all_ingredients:
    solution_2[i] = []
for a, ingredients_list in allergens_dict.items():
    for ingredient in all_ingredients:
        if all([ingredient in ingredients for ingredients in ingredients_list]):
            solution_2[ingredient].append(a)



canonical_dangerous_ingredients = {}

for i in range(0, 8):
    found_ingredient, found_allergen = [s for s in solution_2.items() if len(s[1]) == 1][0]
    found_allergen = found_allergen[0]
    canonical_dangerous_ingredients[found_ingredient] = found_allergen
    for s in solution_2:
        if found_allergen in solution_2[s]:
            solution_2[s].remove(found_allergen)


canonical_dangerous_ingredients = sorted(canonical_dangerous_ingredients.items(), key=lambda x: x[1], reverse=False)
print(",".join([i[0] for i in canonical_dangerous_ingredients]))


