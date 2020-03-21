 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:43:28 2020
@author: don_quixote
"""

"""
1. Write a Python function that takes a sequence of numbers and determines whether all the 
numbers are different from each other. """

def numSeq(num):
    if len(num) == len(set(num)):
        return True
    else:
        return False
n = [1,3,5,6,4,3,3,5,6]
m = [1,2,4,5,6,7,8,9]

print(numSeq(n))
print(numSeq(m))
