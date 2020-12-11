from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=11)
raw = puzzle.input_data
data = raw.splitlines()
ny = len(data)
nx = len(data[0])

def get_grid(data):
    grid = {}
    for i in range(nx):
        for j in range(ny):
            grid[(i,j)] = data[j][i]
    return grid

def check_neighbors(grid,i,j):
    count = 0
    for ii in [i-1,i,i+1]:
        for jj in [j-1, j, j+1]:
            if (ii, jj) != (i,j):
                if(grid.get((ii,jj),'') == '#'):
                    count +=1
    return count

def check_viz_neighbors(grid,i,j):
    count = 0
    for y in [-1,0,1]:
        for x in [-1,0,1]:
            if (x,y) == (0,0):
                continue
            ii = i + x
            jj = j + y
            while 0 <= ii < nx and 0 <= jj < ny:
                if(grid[(ii,jj)] != '.'):
                    if(grid[(ii,jj)] == '#'):
                        count +=1
                    break
                ii += x
                jj += y
    return count

def step_a(grid):
    new_grid = {}
    for j in range(ny):
        for i in range(nx):
            if grid[(i,j)] == '.':
                new_grid[(i,j)] = '.'
            elif grid[(i,j)] == 'L':
                if( not check_neighbors(grid,i,j) ):
                    new_grid[(i,j)] = '#'
                else:
                    new_grid[(i,j)] = 'L'
            elif grid[(i,j)] == '#':
                if check_neighbors(grid,i,j) >= 4:
                    new_grid[(i,j)] = 'L'
                else:
                    new_grid[(i,j)] = '#'
    return new_grid

def step_b(grid):
    new_grid = {}
    for j in range(ny):
        for i in range(nx):
            if grid[(i,j)] == '.':
                new_grid[(i,j)] = '.'
            elif grid[(i,j)] == 'L':
                if( not check_viz_neighbors(grid,i,j) ):
                    new_grid[(i,j)] = '#'
                else:
                    new_grid[(i,j)] = 'L'
            elif grid[(i,j)] == '#':
                if check_viz_neighbors(grid,i,j) >= 5:
                    new_grid[(i,j)] = 'L'
                else:
                    new_grid[(i,j)] = '#'
    return new_grid


def equilibirate(data, step_func):
    grid = get_grid(data)
    while True:
        new_grid = step_func(grid)
        if( new_grid == grid ):
            break
        else:
            grid = new_grid
    print(list(grid.values()).count('#'))

equilibirate(data, step_a)
equilibirate(data, step_b)
