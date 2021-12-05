import numpy as np
from aocd.models import Puzzle
from utils import *

puzzle = Puzzle(year=2021, day=5)
raw = puzzle.input_data
data = [ ints(i) for i in raw.splitlines() ]
data = np.array(data)
xmax = max(data[:,0].max(), data[:,2].max())
ymax = max(data[:,1].max(), data[:,3].max())
canvas1 = np.zeros((xmax+1,ymax+1))
canvas2 = np.zeros((xmax+1,ymax+1))
for x,y, x1,y1 in data:
  dx = np.sign(x1-x)
  dy = np.sign(y1-y)
  if not dx:
    canvas1[x,y:y1+dy:dy] += 1
    canvas2[x,y:y1+dy:dy] += 1
  elif not dy:
    canvas1[x:x1+dx:dx,y] += 1
    canvas2[x:x1+dx:dx,y] += 1
  else:
    for t in range(abs(x-x1)+1):
      canvas2[x+t*dx, y+t*dy] +=1

print(len(np.where(canvas1>1)[0]))
print(len(np.where(canvas2>1)[0]))
