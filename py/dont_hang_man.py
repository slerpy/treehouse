#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# dont_hang_man.py
# --------------------
# A word guessing game.
#
# @author Shaden, 0x899319D4251502BA
# @date  6 January 2016
# @version 0.0.3
##############################################################################

import random

# make a list of words

def letter_flag(letter, word):
    if letter in word:
        return True

def do_underscore(word):
    temp_list = []
    for letter in word:
        if letter == " ":
            temp_list.append(" ")
        else:
            temp_list.append("_")
    return temp_list

def select_random_word(list):   # pick a random word
    return random.choice(list)

def letter_replace(letter, guessed_letters):
    for item in guessed_letters:
        if letter == item:
            item.replace()




def main():
    word_dict = ["apple", "america", "sodapop", "painting", "recycle", "clean", "oscar meyer wiener"]
    game_word = select_random_word(word_dict)
    welcome_message = "Hello and welcome to the word guessing game! Let's get started."
    help_message = "Type QQ to quit, ? for this help."
    wrong_letters = []
    game_word_list = list(game_word)
    guessed_letters = do_underscore(game_word)

    print(welcome_message)
    while True:
        user_input = input("> ")
        if "_" not in guessed_letters:
            print("GRATS!!! YOU WON!!")
            print(welcome_message)
        elif user_input == "QQ":
            print("Awww. See ya next time!")
            break
        elif user_input == "?":
            print(help_message)
            print(game_word)
            print("".join(guessed_letters))
        else:
            if letter_flag(user_input, game_word) == True:
                print("Good guess!")
                index = 0
                for letter in game_word_list:
                    if user_input == letter:
                         guessed_letters[index] = user_input
                    index += 1

                print("".join(guessed_letters))
                continue


            else:
                print("Sorry, Your letter is not in the word.")
                wrong_letters.append(user_input)
                wrong_letters.sort()
                print(wrong_letters)







main()

# draw spaces

# take guess
# draw guessed letters and strikes
# print out win/lose