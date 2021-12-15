import numpy as np
from aocd.models import Puzzle
from utils import *

puzzle = Puzzle(year=2021, day=13)
raw = puzzle.input_data
data, instructions = [x.splitlines() for x in raw.split('\n\n')]
canvas = set([tuple(ints(i)) for i in data])

def fold(canvas, d, loc):
  curr_keys = set(canvas)
  if d == 'x':
    for x,y in curr_keys:
      if x > loc:
        canvas.remove((x,y))
        canvas.add((2*loc - x,y))
  elif d == 'y':
    for x,y in curr_keys:
      if y > loc:
        canvas.remove((x,y))
        canvas.add((x,2*loc - y))
  return canvas

for i,ins in enumerate(instructions):
  d, loc = ins.split('=')
  loc = int(loc)
  canvas = fold(canvas,d[-1],loc)
  if(i == 0):
    print(len(canvas))

grid = np.array(list(canvas))
xmax,ymax = grid.max(axis=0)
for y in range(ymax+1):
      print(''.join('#' if (x,y) in canvas else ' ' for x in range(xmax+1)))
