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

puzzle = Puzzle(year=2019, day=4)
raw = puzzle.input_data
l,h = map(int,raw.split('-'))

def is_valid(pword):
    if len(pword) != 6 or any(pword[i] > pword[i+1] for i in range(5)):
        return False
    numcounts = [pword.count(i) for i in set(pword)]
    if any( i >= 2 for i in numcounts): return True
    return False
p1 = sum( [is_valid(str(i)) for i in range(l, h+1)] )
puzzle.answer_a = p1

def is_valid_new(pword):
    if len(pword) != 6 or any(pword[i] > pword[i+1] for i in range(5)):
        return False
    numcounts = [pword.count(i) for i in set(pword)]
    if any( i == 2 for i in numcounts): return True
    return False
p2 = sum( [is_valid_new(str(i)) for i in range(l, h+1)] )
puzzle.answer_b = p2
