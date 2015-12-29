#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# shopping_list.py
# --------------------
# A quick shopping list
#
# @author Shaden, 0x899319D4251502BA
# @date 28 December 2015
# @version 0.0.1
##############################################################################

shopping_list = ["apples", "oranges", "batteries"]
allowed_commands = ["SHOW", "ADD", "DEL", "HELP", "DONE"]
welcome_message = "Welcome to your shopping list!\nSHOW will list your items\nADD will add new items\nDEL " \
                  "to remove items from the list\n" \
                  "HELP for these instructions.\nDONE to exit.\n" \
                  ">> "
error_message = "I don't understand what you are trying to do\n\n{}".format(welcome_message)
add_message = "Which number slot would you like to add this item? Hit ENTER to insert item at end of list."


def show_list():        # loop through list, print items with numbers to identify them.
    count = 1
    for item in shopping_list:
        print(str(count) + ": " + item)
        count += 1


def insert_item(where, what):       # insert new items into the list
    if where == "" or int(where) > len(shopping_list):  # append to end if <enter> pressed
            shopping_list.append(what)
    else:
        if int(where) >= 1 and int(where) <= len(shopping_list):    # insert at location if specified.
            shopping_list.insert(int(where) - 1, what)


def remove_item(position):          # remove item from list location specified by user
    shopping_list.pop(position - 1)


while True:
    wat = input("> ")
    if wat not in allowed_commands:
        input(error_message)
    elif wat == "DONE":
        print("Goodbye")
        break
    elif wat == "SHOW":
        show_list()
        continue
    elif wat == "DEL":
        show_list()
        remove_item(int(input("Which number would you like to delete?")))
    else:
        if wat == "ADD":
            insert_item(input("where"), input("what"))

    

