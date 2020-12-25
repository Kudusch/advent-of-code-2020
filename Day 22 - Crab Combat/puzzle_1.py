#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input
player_one, player_two = open("input.txt", "r").read().split("\n\n")
player_one = [int(i) for i in player_one.split("\n")[1:]]
player_two = [int(i) for i in player_two.split("\n")[1:]]

round_count = 0
while all([len(player_one) > 0, len(player_two) > 0]):
    winning_cards = sorted([player_one[0], player_two[0]], reverse=True)
    if player_one[0] > player_two[0]:
        player_one.extend(winning_cards)
    else:
        player_two.extend(winning_cards)

    player_one.pop(0)
    player_two.pop(0)
    round_count += 1


if len(player_one) > len(player_two):
    winning_player = player_one.copy()
    print("After round {} player one won!".format(round_count))
else:
    winning_player = player_two.copy()
    print("After round {} player two won!".format(round_count))

score_key = list(reversed(range(1, len(winning_player)+1)))

print(sum([n * score_key[i] for i, n in enumerate(winning_player)]))