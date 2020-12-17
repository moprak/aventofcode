from copy import deepcopy
from aocd.models import Puzzle
from utils import *


puzzle = Puzzle(year=2020, day=14)
raw = puzzle.input_data
data = raw.splitlines()

def apply_mask(mask, value):
    binstr = bin(value)[2:]
    newval = ['']*len(mask)
    for i in range(-len(newval),0):
        if mask[i] != 'X':
            newval[i] = mask[i]
        elif abs(i) <= len(binstr):
            newval[i] = binstr[i]
        else:
            newval[i] = '0'
    return int(''.join(newval), 2)

results={}
for line in data:
    if( line.startswith('mask') ):
        mask = line.split()[2]
    else:
        loc, value = pints(line)
        results[loc] = apply_mask(mask,value)
print(sum(results.values()))

def mem_mask(mask, loc):
    binstr = bin(loc)[2:].rjust(36,'0')
    newval = ['']*len(mask)
    xind = set()
    for i in range(len(mask)):
        if mask[i] == 'X':
            newval[i] = mask[i]
            xind.add(i)
        elif mask[i] == '1':
            newval[i] = mask[i]
        else:
            newval[i] = binstr[i]
    locs = [newval]
    while xind:
        i = xind.pop()
        newlocs = []
        for l in locs:
            newloc = deepcopy(l)
            l[i] = '0'
            newloc[i] = '1'
            newlocs.append(newloc)
        locs.extend(newlocs)
    return [int(''.join(l),2) for l in locs]

results = {}
for line in data:
    if( line.startswith('mask') ):
        mask = line.split()[2]
    else:
        loc, value = pints(line)
        locs = mem_mask(mask,loc)
        for l in locs:
            results[l] = value
print(sum(results.values()))
