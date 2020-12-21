import sys
sys.setrecursionlimit(100000)

import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from aocd import get_data
from functools import reduce
import math
# from blist import blist
# import networkx as nx

from aocd.models import Puzzle
from utils import *


puzzle = Puzzle(year=2020, day=21)
raw = puzzle.input_data
data = raw.splitlines()

ing_counts = defaultdict(int)
alr_candidates = {}
for line in data:
    ing, alr = line.split(' (contains ')
    ing = words(ing)
    alr = words(alr)
    for i in ing:
        ing_counts[i] += 1
    for a in alr:
        if a in alr_candidates:
            alr_candidates[a] &= set(ing)
        else:
            alr_candidates[a] = set(ing)

unsafe = set()
for ing in alr_candidates.values():
    unsafe |= ing
print(sum([ing_counts[i] for i in set(ing_counts.keys()) - unsafe]))

done = set()
solved = {}
while len(solved) < len(alr_candidates):
    for a, ing in alr_candidates.items():
        if a not in solved:
            if len(ing) == 1:
                i = ing.pop()
                solved[a] = i
                done.add(i)
            else:
                alr_candidates[a] -= done
print(','.join([solved[a] for a in sorted(solved.keys())]))
