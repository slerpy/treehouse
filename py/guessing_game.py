#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# guessing_game.py
# --------------------
# A guessing game using python random library
# Game requirements:
# 
# Program picks a random number between 1 and 10.
#
# We ask player to guess the number.
#
# If the guess is wrong we mock them mercilessly and relay whether they
# are high or low, and ask them to guess again.
#
# Once the player is correct, we congratulate them.
#
# We also need to limit their number of guesses, and tell them how many
# guesses they've made and how many they have left.
#
# @author Shaden, 0x899319D4251502BA
# @date  1 December 2015
# @version 0.0.1
##############################################################################

import random


def play_game():
    shh = random.randint(1, 10)     # choose random number between 1 and 10
    number_of_guesses = 0
    allowed_guesses = 10
    print("Please choose a number between 1 and 10")
    while True:

        player_guess = int(input("> "))

        print(shh)
        if player_guess == shh:
            print("Correct! Nice job! You guessed this in {} tries!".format(number_of_guesses + 1))
            break
        elif number_of_guesses < allowed_guesses - 1:
            number_of_guesses += 1
            if player_guess > shh:
                print("Sorry that was not correct. You have {} guesses left! *Hint* You're too high!".format(10 - number_of_guesses))
            else:
                print("Sorry that was not correct. You have {} guesses left! *Hint* You're too low!".format(10 - number_of_guesses))

        else:
            print("Sorry you ran out of guesses.")
            break

play_game()



