import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist
from functools import reduce
from aocd import get_data

raw = get_data(year=2017, day=24)
data = [[int(i) for i in re.findall('-?\d+', line)] for line in raw.splitlines()]
# data = [[0,2],[2,2],[2,3],[3,4],[3,5],[0,1],[10,1],[9,10]]
def find_connectors(w, bridge):
    connectors = [c for c in data if w in c and c not in bridge]
    return connectors

curr = 0
def recurse(w, bridge):
    chips = find_connectors(w, bridge)
    if( len(chips) ):
        for chip in chips:
            if( chip not in bridge ):
                new_bridge = deepcopy(bridge)
                new_bridge.append(chip)
                new_w = chip[0] if chip[1] == w else chip[1]
                for nb in recurse(new_w, new_bridge):
                    yield nb
    else:
        yield bridge

bridges = list(recurse(0,[]))
print('Part A: ', max(map( lambda x: sum( sum(c) for c in x), bridges)))
print('Part B: ', max(map(lambda x: (len(x), sum( sum(c) for c in x)), bridges))[1])
