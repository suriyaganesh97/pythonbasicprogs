#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'setOperation' function below.
#
# The function is expected to return a union, intersection, difference(a,b), difference(b,a), symmetricdifference and frozen set.
# The function accepts following parameters:
#  1. List seta
#  2. List setb
#

def setOperation(seta, setb):
        # Write your code here
    set1=set(seta)
    set2=set(setb)
    un = set1|set2
    #return un
    intersec = set1&set2
    #return intersec
    diffa = set1-set2
    #return diffa
    diffb = set2-set1
    #return diffb
    sydiff = set1^set2
    #return sydiff
    frset=frozenset(seta)
    return un, intersec, diffa, diffb, sydiff, frset

seta = ['apple','orange','grapes','mango','starfruit']
setb = ['papaya','mango','jackfruit','grapes','lychee']
un, intersec, diffa, diffb, sydiff, frset = setOperation(seta, setb)
print(sorted(un))
print(sorted(intersec))
print(sorted(diffa))
print(sorted(diffb))
print(sorted(sydiff))
print("Returned value is {1} frozenset".format(frset, "a" if type(frset) == frozenset else "not a"))