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

def first_4(iter):
    return(iter[:4])

def odds(iter):
    return(iter[1::2])

def first_and_last_4(iter):
    return(iter[0:4] + iter[-4:])

print(first_and_last_4('123456789'))




















