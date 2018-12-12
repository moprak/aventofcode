import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist

data = [[int(i) for i in re.findall('-?\d+', line)] for line in open('input').readlines()]
children = defaultdict(set)
visited = set()
for line in data:
    if(len(line) > 1):
        children[line[0]] = set(line[1:])

def find_group(node):
    visited.add(node)
    for child in children[node]:
        if( child not in visited ):
           find_group(child)
find_group(0)
print('Part A: ', len(visited))
groups = 1
while(len(visited) != len(children)):
    for node in set(children.keys())-visited:
        if(node not in visited):
            find_group(node)
            groups += 1
            break
print('Part B: ', groups)
