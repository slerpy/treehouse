#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# scratchit.py
# --------------------
# simple scratch file, nothing to see here.
#
# @author Shaden, 0x899319D4251502BA
# @date 29 November 2015
# @version 0.0.1
##############################################################################


def add_list(num):
    start_zero = 0
    for e in num:
        start_zero = e + start_zero
    return start_zero


def summarize(list):
    added = add_list(list)
    print("The sum of {} is {}".format(list, added))

summarize([1, 2, 3])
