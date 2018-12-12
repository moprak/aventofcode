import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist
from aocd import get_data
from functools import reduce
raw = get_data(day=14, year=2017)
def knot_hash(raw):
    data = [ ord(i) for i in raw]
    data.extend([17,31,73,47,23])
    state = np.arange(256)
    curr = 0
    skip = 0
    for _ in range(64):
        for i in range(len(data)):
            temp = []
            for j in range(data[i]):
                temp.append(state[(curr+j)%256])
            temp.reverse()
            for j in range(data[i]):
                state[(curr+j)%256] = temp[j]
            curr = (curr + skip + data[i])%256
            skip += 1
    return(''.join('%02x'%reduce(lambda x,y: x^y, state[16*i:16+16*i]) for i in range(16)))

def hash_to_bits(raw):
    return '{:0128b}'.format(int(raw, 16))

canvas = np.empty((128,128), dtype=int)
for i in range(128):
    canvas[i,:] = np.fromiter(map(int, hash_to_bits(knot_hash(f"{raw}-{i}"))),int)
print('Part A: ', canvas.sum())

visited = set()
def recurse(i,j):
    if( (i,j) in visited or canvas[i,j] == 0):
        return
    visited.add((i,j))
    if(i < 127):
        recurse(i+1,j)
    if(j < 127):
        recurse(i,j+1)
    if(i > 0):
        recurse(i-1,j)
    if(j > 0):
        recurse(i,j-1)
    return
groups = 0
for i in range(128):
    for j in range(128):
        if( (i,j) in visited or canvas[i,j] == 0):
            continue
        recurse(i,j)
        groups += 1
print('Part B: ', groups)
