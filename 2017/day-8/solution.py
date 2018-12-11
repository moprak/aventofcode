import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase
from copy import deepcopy
from blist import blist

data = [ line.strip().split() for line in open('input').readlines() ]
state = defaultdict(int)

def compare(a, op, b):
    return{
            '==': a == b,
            '!=': a != b,
            '>': a > b,
            '<': a < b,
            '>=': a >= b,
            '<=': a <= b
            }[op]

maxval = 0
for var, inc, delta, _, dep, op, val in data:
    delta = int(delta)
    if( compare(state[dep], op, int(val) )):
            state[var] = state[var] + delta if inc =='inc' else state[var] - delta
            maxval = max(state[var],maxval)
print('Part A: ', max(state.values()))
print('Part B: ', maxval)
