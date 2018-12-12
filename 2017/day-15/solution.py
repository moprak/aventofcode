import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist
from aocd import get_data
from functools import reduce

raw = get_data(year=2017,day=15)
data = [int(i) for i in re.findall('-?\d+', raw)]

factors = [16807, 48271]
M = 2147483647

def genA(check=0):
    a = data[0]
    while True:
        a *= factors[0]
        a %= M
        if( check ):
            if( a%check == 0):
                yield a
        else:
            yield a

def genB(check=0):
    b = data[1]
    while True:
        b *= factors[1]
        b %= M
        if( check ):
            if( b%check == 0):
                yield b
        else:
            yield b

def compare(a,b):
    return a & 0xFFFF == b & 0xFFFF

match = 0
i=0
a = genA()
b = genB()
while i < 40e6:
    if compare(next(a),next(b)): match += 1
    i+=1
print('Part A: ', match)

match = 0
i=0
a = genA(4)
b = genB(8)
while i < 5e6:
    if compare(next(a),next(b)): match += 1
    i+=1
print('Part B: ', match)
