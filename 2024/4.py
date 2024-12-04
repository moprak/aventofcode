import numpy as np
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=4)
raw = puzzle.input_data
data = []
for row in raw.splitlines():
    data.append(list(row))
data = np.array(data)
ny, nx = data.shape

p1 = 0
for j in range(ny):
    for i in range(nx):
        lines = []
        if i < nx - 3:
            lines.append("".join(data[j, i + k] for k in range(4)))
        if i < nx - 3 and j < ny - 3:
            lines.append("".join(data[i + k, j + k] for k in range(4)))
        if i < nx - 3 and j > 2:
            lines.append("".join(data[i + k, j - k] for k in range(4)))
        if j < ny - 3:
            lines.append("".join(data[j + k, i] for k in range(4)))
        p1 += lines.count("XMAS") + lines.count("SAMX")
print(p1)

p2 = 0
for j in range(1, ny - 1):
    for i in range(1, nx - 1):
        d1 = "".join(data[j + k, i + k] for k in range(-1, 2))
        d2 = "".join(data[j - k, i + k] for k in range(-1, 2))
        if (d1 == "SAM" or d1 == "MAS") and (d2 == "SAM" or d2 == "MAS"):
            p2 += 1

print(p2)
