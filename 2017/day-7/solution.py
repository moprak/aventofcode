import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase
from copy import deepcopy
from blist import blist

data = [ re.findall('\w+', line) for line in open('input').readlines() ]

all_children = set()
nodes = {}
children = {}
parents = {}
graph = defaultdict(set)
weights = defaultdict(int)
is_balanced = {}
for line in data:
    nodes[line[0]] = int(line[1])
    children[line[0]] = line[2:]
    for node in line[2:]:
        all_children.add(node)
        parents[node] = line[0]
root = (nodes.keys() - parents.keys()).pop()
print('Part A: ', root)

def recurse(node):
    weights[node] = nodes[node]
    cws = {}
    for child in children[node]:
        cw = recurse(child)
        cws[child] = cw
    if(len(children[node]) > 1):
        for c in cws:
            if( list(cws.values()).count(cws[c]) == 1):
                delta = (set(cws.values()) - set([cws[c]])).pop() - cws[c]
                cws[c] += delta
                print('Part B: ', nodes[c]+delta)
    for w in cws.values():
        weights[node] += w

    return weights[node]
recurse(root)
