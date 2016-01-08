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



import random


def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2


def ok():
    start = 5
    while start:
        randomy = random.randint(1,99)
        if even_odd(randomy) is True:
            print("{} is even".format(randomy))
            start -= 1
        else:
            print("{} is odd".format(randomy))
            start -= 1

ok()
