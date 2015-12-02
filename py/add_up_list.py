#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# add_up_list.py
# --------------------
# Simple script to add up a list of integers.
#
# @author Shaden, 0x899319D4251502BA
# @date  1 December 2015
# @version 0.0.1
##############################################################################


def add_list(num):  # loop through our list and add it up.
    start_zero = 0
    for e in num:
        start_zero = e + start_zero
    return start_zero


def summarize(int_list):    # send our list up into the add_list function
    added = add_list(int_list)
    print("The sum of {} is {}".format(int_list, added))

summarize([3, 2, 3])
    

