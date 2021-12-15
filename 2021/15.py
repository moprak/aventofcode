import numpy as np
from aocd.models import Puzzle
from heapq import heappop, heappush

puzzle = Puzzle(year=2021, day=15)
raw = puzzle.input_data
data = np.asarray([list(i) for i in raw.splitlines()], dtype=int)
nx,ny = data.shape
neighbors = [(0,1),(1,0),(-1,0),(0,-1)]

def get_distance(factor):
  heap = [(0, 0, 0)]
  seen = {(0, 0)}
  while heap:
    distance, x, y = heappop(heap)
    if (x,y) == (factor*nx-1, factor*ny-1):
      return(distance)

    for dx, dy in neighbors:
      xx, yy = x + dx, y + dy
      if 0 <= xx < factor*nx and 0 <= yy < factor*ny:
        if (xx, yy) not in seen:
          seen.add((xx, yy))
          sx,xp = divmod(xx,nx)
          sy,yp = divmod(yy,ny)
          val = (data[xp,yp] + sx + sy - 1)%9 + 1
          heappush(heap, (distance + val, xx, yy))

print(get_distance(1))
print(get_distance(5))
