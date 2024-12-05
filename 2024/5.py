from aocd.models import Puzzle
import utils
from functools import cmp_to_key


puzzle = Puzzle(year=2024, day=5)
raw = puzzle.input_data
rules = raw.split("\n\n")[0]
data = raw.split("\n\n")[1]
rules = [utils.ints(i) for i in rules.splitlines()]
data = [utils.ints(i) for i in data.splitlines()]


def order(a, b):
    for l, r in rules:
        if a == r and b == l:
            return 1
        elif a == l and b == r:
            return -1
    return 0


p1 = 0
p2 = 0
to_correct = []
for row in data:
    valid = all(
        (l not in row) or (r not in row) or (row.index(l) < row.index(r))
        for l, r in rules
    )
    if valid:
        p1 += row[len(row) // 2]
    else:
        corrected = sorted(row, key=cmp_to_key(order))
        p2 += corrected[len(corrected) // 2]
print(p1)
print(p2)
