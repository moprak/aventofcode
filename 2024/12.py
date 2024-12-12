from aocd.models import Puzzle
import numpy as np


puzzle = Puzzle(year=2024, day=12)
raw = puzzle.input_data
grid = {
    i + j * 1j: c for i, row in enumerate(raw.splitlines()) for j, c in enumerate(row)
}


def find_region(x):
    to_check = set([x])
    region = set([x])
    while len(to_check):
        cx = to_check.pop()
        for delta in [1, -1, 1j, -1j]:
            new = cx + delta
            if (new not in region) and (new in grid) and (grid[new] == grid[x]):
                to_check.add(new)
                region.add(new)
    return region


def perimeter(region):
    perimeter = 0
    sides = 0
    for cx in region:
        for delta in [1, -1, 1j, -1j]:
            if cx + delta not in region:
                perimeter += 1
                if (cx + 1j * delta not in region) or (
                    cx + 1j * delta + delta in region
                ):
                    sides += 1

    return np.array([perimeter, sides], dtype=int)


seen = set()
res = np.zeros(2, dtype=int)
for k in grid:
    if k not in seen:
        region = find_region(k)
        seen = seen | region
        res += len(region) * perimeter(region)

print(res)
