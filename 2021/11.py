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


puzzle = Puzzle(year=2021, day=11)
raw = puzzle.input_data
data = [list(i) for i in raw.splitlines()]
data = np.asarray(data,dtype=int)
nx,ny = data.shape
neighbors = [(0,1),(0,-1),(1,0),(-1,0)]
neighborsd = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]

def step(data):
  flashes = 0
  data = data+1
  q = set([idx for idx in zip(*np.where(data>9))])
  while q:
    i,j = q.pop()
    data[i,j] = 0
    flashes += 1
    for dx,dy in neighborsd:
      ii, jj = i+dx, j+dy
      if 0<= ii < nx and 0 <= jj < ny and data[ii,jj]:
        data[ii,jj] += 1
        if( data[ii,jj] > 9):
          q.add((ii,jj))
  return data, flashes

p1 = 0
d2 = data.copy()
for _ in range(100):
  data,f = step(data)
  p1 += f
print(p1)

p2 = 0
ctr = 0
while not p2:
  d2, _ = step(d2)
  ctr += 1
  if not np.sum(d2):
    p2 = ctr
print(p2)
