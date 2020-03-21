#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 22:25:30 2020

@author: don_quixote
"""


""" 5. Write a Python program to count the number of strings where the string length is 2 
or more and the first and last character are same from a given list of strings """


def countstring(s):
    c = 0
    for i in s:
        if len(i) == 2:
            c = c + 1
            
    return c
str1 = ["abds" , "ab" , "kuwd" , "hgs", "ud" , "sy", "abs", "ab", "ufjs" , "apo" ,"ah"]

print(countstring(str1))
            