#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# tupgame.py
# --------------------
# Game where we spawn an entity on random coordinates and try to get around. Really just
# an exercise in random tuples.
#
# @author Shaden, 0x899319D4251502BA
# @date  8 February 2016
# @version 0.0.1
##############################################################################

import random

# Our locations - Expand much further, later.
CELLS = [(0, 0), (0, 1), (0, 2),
         (1,0), (1, 1), (1, 2),
         (2, 0), (2, 1), (2, 2)]


def get_location():
    enemy = random.choice(CELLS)    # spawn enemy in random location
    exit_door = random.choice(CELLS)    # spawn exit in a random location
    player = random.choice(CELLS)   # spawn player in a random location

    #  if any of our spawn cells are same, do it again, otherwise return relevant locations.
    while enemy == exit_door or exit_door == player or player == enemy:
        enemy = random.choice(CELLS)
        exit_door = random.choice(CELLS)
        player = random.choice(CELLS)
        print("W00ps, a match -- Cycling")  # TESTING - remove
    else:
        return enemy, exit_door, player







#def move_player(player, move):
    # get the players current location
    # if move is left y - 1
    # if move is right y + 1
    # if move is up x - 1
    # if move is down x + 1
#    return player

def get_moves(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
#    if player# if player y is 0, remove left
    # if player x is 0, remove up
    # if player y is 2, remove right
    # if player x is 2, remove down
    return MOVES

# while True:
#     print("Welcome to the escape!")
#     print("You're currently in room {}") # fill in with our position
#     print("You can move {}") # fill in with available moves
#     print("Enter QUIT to quit")
#
#     move = input("> ")
#     move = move.upper()
#
#     if move == 'QUIT':
#         break
#
#     # if move is allowed, change players position
#     # if move is illegal, dont change anything
#     # if position is exit, THEY WIN!
#     # if the position is the monster, they lose.
#     # else continue

print(get_location())