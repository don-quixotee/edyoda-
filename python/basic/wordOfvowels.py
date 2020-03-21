#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:51:48 2020

@author: don_quixote
"""


""" 2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. 
Use the characters exactly once """
import random

s = ['a', 'e' , 'i', 'o', 'u']
for num in range(len(s)):
    random.shuffle(s)
    print(''.join(s))