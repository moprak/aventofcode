import numpy as np
from collections import deque
from aocd.models import Puzzle
from utils import *

puzzle = Puzzle(year=2021, day=9)
raw = puzzle.input_data
data = raw.splitlines()
d = np.array([[int(i) for i in list(d)] for d in data])
ny,nx = d.shape
neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

p1 = 0
low_points = []
for i in range(ny):
  for j in range(nx):
    flag = True
    for dy,dx in neighbors:
      ii, jj = i+dy, j+dx
      if (0 <= ii < ny and 0 <= jj < nx) and d[ii,jj] <= d[i,j]:
        flag = False
    if flag:
      p1 += d[i,j] + 1
      low_points.append((i,j))
print(p1)

areas = []
seen = set()
for lp in low_points:
  q = deque()
  seen = set()
  q.append(lp)
  basin = 1
  while q:
    i,j = q.popleft()
    seen.add((i,j))
    for dy,dx in neighbors:
      ii, jj = i+dy, j+dx
      if (ii,jj) not in seen and (0 <= ii < ny and 0 <= jj < nx) and d[ii,jj] != 9 :
        q.append((ii,jj))
        basin += 1
      seen.add((ii,jj))
  areas.append(basin)
areas = sorted(areas)
p2 = prod(areas[-3:])
print(p2)
