import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase
from copy import deepcopy
from blist import blist

data = open('input').read().strip()
i = 0
score = 0
curr_level = 0
is_garbage = 0
garbage = 0
while i < len(data):
    if data[i] == '!':
        i += 1
    elif is_garbage:
        if data[i] == '>':
            is_garbage = 0
        else:
            garbage += 1
    elif data[i] == '{':
        curr_level += 1
        score += curr_level
    elif data[i] == '}':
        curr_level -=1
    elif data[i] == '<':
        is_garbage = 1
    i += 1
print('Part A: ', score)
print('Part B: ', garbage)
