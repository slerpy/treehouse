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
def random_item(iter):
    print(iter[random.randint(0,len(iter) -1)])

random_item("Random String")