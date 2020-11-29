import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist
from aocd import get_data
from functools import reduce
from aocd.models import Puzzle
import math

puzzle = Puzzle(year=2019, day=16)
raw = puzzle.input_data
data = [ int(i) for i in raw ]

d = np.array(data,dtype=int)
base_patt = [0,1,0,-1]

for _ in range(100):
    d_new = np.copy(d)
    for i in range(len(d)):
        pi = np.repeat(base_patt,i+1)
        pi_tile = np.tile(pi, math.ceil(len(d)/(len(pi)-1)))
        d_new[i] = abs(d.dot(pi_tile[1:len(d)+1]))%10
    d = d_new
puzzle.answer_a = ''.join([str(i) for i in d[:8]])


d_new = data*10000
offset = int(''.join(map(str, d_new[:7])))
relevant = d_new[offset:]
for _ in range(100):
    for i in range(-2,-len(relevant)-1, -1):
        relevant[i] = (relevant[i]+relevant[i+1])%10
puzzle.answer_b = ''.join([str(i) for i in relevant[:8]])
