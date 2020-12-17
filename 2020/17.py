from collections import defaultdict
from aocd.models import Puzzle


puzzle = Puzzle(year=2020, day=17)
raw = puzzle.input_data
data = raw.splitlines()
nx,ny = len(data[0]), len(data)

def get_grid(data):
    grid = defaultdict(int)
    z,w = 0,0
    for i,line in enumerate(data):
        for k, c in enumerate(line):
            if line[k] == '#':
                grid[(k,i,z,w)] = 1
    return grid

def get_score(point):
    active = 0
    x,y,z,w = point
    for dw in (-1,0,1):
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                for dz in (-1,0,1):
                    if (dx,dy,dz,dw) !=(0,0,0,0):
                        if( grid[(x+dx,y+dy,z+dz,w+dw)] == 1 ):
                            active += 1
    return active

def run_step(grid, step, parta = True):
    x_min,y_min,z_min = -step -1, -step-1, -step -1
    x_max,y_max,z_max = step + nx, step + ny, step + 1

    if( parta ):
        w_min = 0
        w_max = 0
    else:
        w_min = -step -1
        w_max = -(w_min)

    new_grid = defaultdict(int)
    for w in range(w_min, w_max +1):
        for x in range(x_min, x_max+1):
            for y in range(y_min, y_max+1):
                for z in range(z_min, z_max+1):
                    point = (x,y,z,w)
                    score = get_score(point)
                    if grid[point] == 0 and score == 3:
                        new_grid[point] = 1
                    if grid[point] == 1 and ( score in (2,3) ):
                        new_grid[point] = 1
    return new_grid

grid = get_grid(data)
for i in range(6):
    grid = run_step(grid, i)
print(list(grid.values()).count(1))

grid = get_grid(data)
for i in range(6):
    grid = run_step(grid,i,False)
print(list(grid.values()).count(1))
