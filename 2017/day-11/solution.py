import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist

data = open('input').read().strip().split(',')
dists = []
def get_dist(data):
    counts = Counter(data)
    reduced = {}
    if( counts['ne'] > counts['sw'] ):
        reduced['ne'] = counts['ne'] - counts['sw']
    else:
        reduced['sw'] = - (counts['ne'] - counts['sw'])

    if( counts['se'] > counts['nw'] ):
        reduced['se'] = counts['se'] - counts['nw']
    else:
        reduced['nw'] = - (counts['se'] - counts['nw'])

    if(counts['n'] > counts['s']):
        reduced['n'] = counts['n'] - counts['s']
    else:
        reduced['s'] = -(counts['n'] - counts['s'])
    if set(reduced.keys()) == set(['sw','nw','s']): return max(reduced['nw'],reduced['s']) + reduced['sw']
    if set(reduced.keys()) == set(['sw','nw','n']): return max(reduced['sw'],reduced['n']) + reduced['nw']
    if set(reduced.keys()) == set(['se','ne','s']): return max(reduced['ne'],reduced['s']) + reduced['se']
    if set(reduced.keys()) == set(['se','ne','n']): return max(reduced['se'],reduced['n']) + reduced['ne']
    if set(reduced.keys()) == set(['ne','nw','s']) or set(reduced.keys()) == set(['se','sw','n']): return  max(reduced.values()) - min(reduced.values())
    if set(reduced.keys()) == set(['se','sw','s']): return max(reduced['se'],reduced['sw']) + reduced['s']
    if set(reduced.keys()) == set(['ne','nw','n']): return max(reduced['ne'],reduced['nw']) + reduced['n']
print('Part A: ', get_dist(data))

for i in range(len(data)):
    dists.append(get_dist(data[:i+1]))
print('Part B: ', max(dists))
