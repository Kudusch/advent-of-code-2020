#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read puzzle input
player_one, player_two = open("input.txt", "r").read().split("\n\n")
player_one = [int(i) for i in player_one.split("\n")[1:]]
player_two = [int(i) for i in player_two.split("\n")[1:]]


def play_combat(deck_one, deck_two):
    played_configurations = []
    while all([len(deck_one) > 0, len(deck_two) > 0]):
        deck_one_copy = deck_one.copy()
        deck_two_copy = deck_two.copy()
        if [deck_one, deck_two] in played_configurations:
            raise SystemExit(played_configurations[-2], 0)
        print("\t", len(played_configurations))
        drawn_cards = [deck_one[0], deck_two[0]]
            
        print("Player 1:", deck_one)
        print("Player 2:", deck_two)
        print("Drawn cards:", drawn_cards)
            
        deck_one.pop(0)
        deck_two.pop(0)
        if len(deck_one) >= drawn_cards[0] and len(deck_two) >= drawn_cards[1]:
            print("\tEntering subgame")
            # try:
            #     deck_one_subgame, deck_two_subgame = play_combat(deck_one[0:drawn_cards[0]], deck_two[0:drawn_cards[1]])
            #     if len(deck_one_subgame) > len(deck_two_subgame):
            #         deck_one.extend(drawn_cards)
            #     else:
            #         deck_two.extend(list(reversed(drawn_cards)))
            # except:
            #     deck_one.extend(drawn_cards)
            deck_one_subgame, deck_two_subgame = play_combat(deck_one[0:drawn_cards[0]], deck_two[0:drawn_cards[1]])
            if len(deck_one_subgame) > len(deck_two_subgame):
                deck_one.extend(drawn_cards)
            else:
                deck_two.extend(list(reversed(drawn_cards)))
            print("\tReturning form subgame")
        else:
            if drawn_cards[0] > drawn_cards[1]:
                deck_one.extend(sorted(drawn_cards, reverse=True))
            else:
                deck_two.extend(sorted(drawn_cards, reverse=True))
        played_configurations.append([deck_one_copy, deck_two_copy])
    return(deck_one, deck_two)


try:
    player_one, player_two = play_combat(player_one, player_two)
except SystemExit as err:
    winning_player_deck = err.args[1]
    winning_player = "1"

if len(player_one) > len(player_two):
    winning_player_deck = player_one.copy()
    winning_player = "1"
else:
    winning_player_deck = player_two.copy()
    winning_player = "2"


score_key = list(reversed(range(1, len(winning_player_deck)+1)))    
points = sum([n * score_key[i] for i, n in enumerate(winning_player_deck)])
print("Player {} won with {} points!".format(winning_player, points))