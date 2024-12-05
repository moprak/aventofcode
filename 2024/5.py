from functools import cmp_to_key
from aocd.models import Puzzle
import utils

puzzle = Puzzle(year=2024, day=5)
raw = puzzle.input_data
rules, data = raw.split("\n\n")
rules = [utils.ints(i) for i in rules.splitlines()]
data = [utils.ints(i) for i in data.splitlines()]


# Trick from 4HbQ
# We -1 only if a < b is in rules
def order(a, b):
    return 1 - 2 * ([a,b] in rules)

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
