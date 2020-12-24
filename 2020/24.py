import re
from collections import defaultdict
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=24)
raw = puzzle.input_data
data = raw.splitlines()

# representing a hex-grid with (x,y,z) where x+y+z = 0,
# z is left out since it's redundant
deltas = {'e': ( 1,-1),
          'w': (-1, 1),
          'ne':( 1, 0),
          'sw':(-1, 0),
          'nw':( 0, 1),
          'se':( 0,-1)}

grid = defaultdict(int)
for line in data:
    x,y = (0,0)
    dirs = re.findall('|'.join(deltas.keys()), line)
    for d in dirs:
        delta = deltas[d]
        x += delta[0]
        y += delta[1]

    if( grid[(x,y)] ):
        grid[(x,y)] = 0
    else:
        grid[(x,y)] = 1

print('Part 1:', sum(grid.values()))

def get_score(x,y, grid):
    return sum( grid[(x+d[0], y+d[1])] for d in deltas.values())

def move(grid):
    newgrid = defaultdict(int)
    score = defaultdict(int)
    curr_keys = list(grid.keys())
    for k in curr_keys:
        score[k] = get_score(*k, grid)
        for d in deltas.values():
            kk = (k[0]+d[0], k[1]+d[1])
            score[kk] = get_score(*kk,grid)
    for k, s in score.items():
        if grid[k] and ( 0 < s <= 2 ):
            newgrid[k] = 1
        if (not grid[k]) and s ==2:
            newgrid[k] = 1
    return newgrid

for _ in range(100):
    grid = move(grid)
print('Part 2:', sum(grid.values()))
