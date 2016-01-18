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


def word_count(strang):
    easify = strang.lower().split()
    easify_dict = {}
    for each in easify:
        if each in easify_dict:
            easify_dict[each] += 1
        else:
            easify_dict[each] = 1
    return easify_dict


dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I'm fucking craving {food}!"


def string_factory():
    new_list = []
    count = 0
    for each in dicts:
        new_list.append(string.format(**dicts[count]))
        count += 1
    return new_list


traveler_dictionary = {'Random Person 01': ['Place Traveled 1', 'Place Traveled 2', 'Place Traveled 3'], 'Random Person 02': ['Place Traveled 01', 'Place Traveled 02'], 'Random Person 03': ['Place Traveled One', 'Place Traveled Two', 'Place Traveled Three', 'Place Traveled Four']}


def most_traveled_person(travelers):
    max_count = 0
    current_winner = ""
    for traveler in travelers:

        if len(travelers[traveler]) > max_count:
            max_count = len(travelers[traveler])
            current_winner = traveler
    print(current_winner)


def num_travelers(travelers):
    return len(travelers.values())


def stats_travelers(travelers):
    temp_list = []
    for traveler in travelers:
        temp_list.append([traveler, len(travelers[traveler])])
    print(temp_list[0])

def places_traveled(travelers):
    traveled_list = []
    for traveler in travelers:
        for places in travelers[traveler]:
            traveled_list.append(places)
    print(traveled_list)

#places_traveled(traveler_dictionary)




def stringcases(string):
    return string.lower(), string.upper(), string.title(), string[::-1]


def combo(tup1, tup2):
    return list(zip(tup1, tup2))



combo([1,2,3,4,5], "oh my")



