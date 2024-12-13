import numpy as np
from aocd.models import Puzzle
from utils import ints


def score(data, offset=0):
    a1, a2 = data[0]
    b1, b2 = data[1]
    c1, c2 = data[2] + offset
    denom = a1 * b2 - a2 * b1
    x = (c1 * b2 - c2 * b1) // denom
    y = (c2 * a1 - c1 * a2) // denom
    if np.all(x * data[0] + y * data[1] == data[2] + offset):
        return 3 * x + y
    return 0

def score_numpy(data, offset = 0):
    tol = 1e-16 * offset + 1e-8 # 1e-8 for when offset is small
    presses = np.linalg.solve(data[:2].T, data[2]+offset)
    if np.all(np.abs(np.round(presses) - presses) < tol):
        return round(presses.dot([3,1]))
    return 0

puzzle = Puzzle(year=2024, day=13)
raw = puzzle.input_data
offset = 10000000000000
items = raw.split("\n\n")

p1, p2 = 0, 0
for item in items:
    data = np.array([ints(i) for i in item.splitlines()], dtype=int)
    p1 += score(data)
    p2 += score(data, offset)

print(int(p1))
print(int(p2))
