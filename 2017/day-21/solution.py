import numpy as np
from aocd import get_data

raw = get_data(day=21,year=2017)
data = [ line.strip().split() for line in raw.splitlines() ]
init = '.#./..#/###'
recipe = {}
for line in data:
    inp, out = line[0], line[2]
    inp = np.array([[c == '#' for c in b] for b in inp.split('/')])
    out = np.array([[c == '#' for c in b] for b in out.split('/')])
    flip = np.fliplr(inp)
    for i in range(4):
        recipe[np.rot90(inp,i).tostring()] = out
        recipe[np.rot90(flip,i).tostring()] = out

def grow(grid):
    size = len(grid)
    if size % 2 == 0:
        cells = size // 2
        newgrid = np.empty((3*cells, 3*cells), dtype=bool)
        for i in range(cells):
            for j in range(cells):
                newgrid[i*3:i*3+3,j*3:j*3+3] = recipe[grid[i*2:i*2+2,j*2:j*2+2].tostring()]
    elif size % 3 == 0:
        cells = size // 3
        newsize = cells * 4
        newgrid = np.empty((4*cells, 4*cells), dtype=bool)
        for i in range(cells):
            for j in range(cells):
                newgrid[i*4:i*4+4,j*4:j*4+4] = recipe[grid[i*3:i*3+3,j*3:j*3+3].tostring()]
    return(newgrid)

grid = np.array([[c == '#' for c in b] for b in init.split('/')])
for i in range(18):
    if( i == 5 ): print('Part A: ', grid.sum())
    grid = grow(grid)
print('Part B: ', grid.sum())
