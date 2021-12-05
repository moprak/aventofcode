import numpy as np
from aocd.models import Puzzle
from utils import *
from collections import defaultdict

puzzle = Puzzle(year=2021, day=5)
raw = puzzle.input_data
data = [ ints(i) for i in raw.splitlines() ]
canvas1 = defaultdict(int)
canvas2 = defaultdict(int)
for x,y, x1,y1 in data:
  dx = np.sign(x1-x)
  dy = np.sign(y1-y)
  for t in range(max(abs(x-x1),abs(y-y1))+1):
    canvas2[x+t*dx, y+t*dy] +=1
    if not dx or not dy:
      canvas1[x+t*dx, y+t*dy] +=1

print(len([v for v in canvas1.values() if v > 1]))
print(len([v for v in canvas2.values() if v > 1]))
