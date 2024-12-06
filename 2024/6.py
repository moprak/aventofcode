import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=6)
raw = puzzle.input_data
data = np.array([list(r) for r in raw.splitlines()])
starty, startx = np.where(data == "^")
start = (starty[0], startx[0])


def run_path(start, data, ymod=None, xmod=None):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    cdir = 0
    ny, nx = data.shape
    y, x = start
    path = {(y, x)}
    visited = {(y, x, cdir)}
    while True:
        dy, dx = dirs[cdir % 4]
        newx, newy = x + dx, y + dy
        if newx < 0 or newx == nx or newy < 0 or newy == ny:
            break
        if data[newy, newx] == "#" or ((newy, newx) == (ymod, xmod)):
            cdir = (cdir + 1) % 4
            continue
        else:
            y, x = newy, newx
            if (y, x, cdir) in visited:
                return path, True
            visited.add((y, x, cdir))
            path.add((y, x))
    return path, False


path, is_loop = run_path(start, data)
print(len(path))

p2 = 0
for ly, lx in path:
    if (ly, lx) == start:
        continue
    _, is_loop = run_path(start, data, ymod=ly, xmod=lx)
    p2 += is_loop
print(p2)
