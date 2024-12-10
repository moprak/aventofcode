from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2024, day=10)
raw = puzzle.input_data
data = np.array(
    [np.array(list(map(int, list(i))), dtype=int) for i in raw.splitlines()], dtype=int
)


def score(tx, ty, data):
    to_check = [[tx,ty]]
    peaks = set()
    paths = 0
    while len(to_check):
        cx, cy = to_check.pop()
        if data[cx, cy] == 9:
            peaks.add((cx, cy))
            paths += 1
        else:
            for i, j in [(cx, cy + 1), (cx, cy - 1), (cx - 1, cy), (cx + 1, cy)]:
                if 0 <= i < data.shape[0] and 0 <= j < data.shape[1]:
                    if data[i, j] == data[cx, cy] + 1:
                        to_check.append([i, j])
    return len(peaks), paths


p1, p2 = 0, 0
for tx, ty in zip(*np.where(data == 0)):
    t1, t2 = score(tx, ty, data)
    p1 += t1
    p2 += t2
print(p1)
print(p2)
