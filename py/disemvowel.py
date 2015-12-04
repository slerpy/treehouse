#!/usr/bin/env python
#-*- coding: utf-8 -*-
##############################################################################
#
# disemvowel.py
# --------------------
# Super useful script to remove vowels from any given words.

# Try and except blocks which removes vowels from any given words. Return
# list of words with first letter capitalized.
#
# @author Shaden, 0x899319D4251502BA
# @date  2 December 2015
# @version 0.0.1
##############################################################################

# Split sentence into a list of words
#     Split each word into a list(word)
#         Remove each vowel from keyword
#             reassemble voweless word
#     reassemble sentence
# capitalize each sentence.


phrase = "Man is least himself when he talks in his own person. Give him a mask, and he will tell you the truth."

vowels = list('aeiou')



def phrase_split(to_split):
    return(to_split.split())


def word_split(to_split):
    return(list(to_split))


def vowel_test(letter):
    for vowel in vowels:
        if vowel == letter:
            return "true"


def devowel(word):
    for each in word:
        if vowel_test(each) == "true":
            word.remove(each)
    return(word)

def bringing_it_together():
    reassembled = []
    brokeass_words = []
    split_phrase = phrase_split(phrase)
    for each in split_phrase:
        brokeass_words.append(word_split(each))
    print(brokeass_words)
    for each in brokeass_words:
        reassembled.append(devowel(each))

    print(reassembled)






bringing_it_together()

