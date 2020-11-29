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

puzzle = Puzzle(year=2019, day=14)
raw = puzzle.input_data
data = [ [ part.split(',') for part in line.strip('\n').split(sep='=>')] for line in raw.splitlines() ]

reactions = {}
for rxn in data:
    lhs = {}
    for comp in rxn[0]:
        splits = comp.strip().split()
        lhs[splits[1]] = int(splits[0])
    rhs = rxn[1][0].strip().split()
    reactions[rhs[1]] = [int(rhs[0]), lhs]

def get_ores(reactions, amount = 1):
    ores = 0
    rxn_queue = defaultdict(int)
    ore_queue = defaultdict(int)
    rxn_queue['FUEL'] = amount
    slack = defaultdict(int)
    while rxn_queue:
        comp, qty = rxn_queue.popitem()
        if comp == 'ORE':
            ores += qty
        else:
            if( qty <= slack[comp] ):
                slack[comp] -= qty
            else:
                qty -= slack[comp]
                intqty = int(np.ceil((qty)/reactions[comp][0]))
                slack[comp] = intqty*reactions[comp][0] - qty
                for new_comp, new_val in reactions[comp][1].items():
                    rxn_queue[new_comp] += intqty*new_val
    return ores
puzzle.answer_a = get_ores(reactions)

ores = 10**12
min_guess = ores//get_ores(reactions)
max_guess = min_guess*8
while (max_guess - min_guess) > 1:
    mid = (min_guess + max_guess)//2
    if(get_ores(reactions, mid) > ores):
        max_guess = mid
    else:
        min_guess = mid

puzzle.answer_b = min_guess
