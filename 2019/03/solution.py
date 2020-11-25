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

op = {'U' : np.array([ 0, 1]),
      'D' : np.array([ 0,-1]),
      'R' : np.array([ 1, 0]),
      'L' : np.array([-1, 0]),
  }
puzzle = Puzzle(year=2019, day=3)
raw = puzzle.input_data
data = [ line.strip('\n').split(sep=',') for line in raw.splitlines() ]

def map_path(wire):
    current = np.zeros(2)
    xlines = []
    ylines = []
    dist = 0
    for e in wire:
        if e[0] in ['U','D']:
            yline = np.zeros(5)
            yline[0] = current[0]
            y1 = current[1]
            current += op[e[0]]*int(e[1:])
            y2 = current[1]
            yline[1:3] = np.sort([y1,y2])
            yline[3] = dist
            dist += yline[2] - yline[1]
            yline[4] = y1
            ylines.append(yline)
        elif e[0] in ['L','R']:
            xline = np.zeros(5)
            xline[0] = current[1]
            x1 = current[0]
            current += op[e[0]]*int(e[1:])
            x2 = current[0]
            xline[1:3] = np.sort([x1,x2])
            xline[3] = dist
            dist += xline[2] - xline[1]
            xline[4] = x1
            xlines.append(xline)
    return xlines,ylines

p1 = map_path(data[0])
p2 = map_path(data[1])

def get_intersection(xline, yline):
    if (yline[1] <= xline[0] <= yline[2]) and (xline[1] <= yline[0] <= xline[2]):
        return (abs(xline[0]) + abs(yline[0])), (xline[3] + yline[3] + abs(xline[4] - yline[0]) + abs(yline[4] - xline[0]))
    return -1,-1
minres = 1e9
minstep = 1e9
for xline in p1[0]:
    for yline in p2[1]:
        res, step = get_intersection(xline, yline)
        if(res > 0 ):
            minres = min(minres, res)
            minstep = min(minstep, step)
for xline in p2[0]:
    for yline in p1[1]:
        res, step = get_intersection(xline, yline)
        if(res > 0 ):
            minres = min(minres, res)
            minstep = min(minstep, step)

puzzle.answer_a = int(minres)
puzzle.answer_b = int(minstep)
