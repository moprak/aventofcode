from aocd.models import Puzzle
import utils

puzzle = Puzzle(year=2024, day=2)
raw = puzzle.input_data
data = [utils.ints(i) for i in raw.splitlines()]


def is_safe(row):
    all_inc = True
    all_dec = True
    for i in range(1, len(row)):
        diff = abs(row[i - 1] - row[i])
        if diff > 3 or diff == 0:
            return False
        all_inc = all_inc and row[i - 1] < row[i]
        all_dec = all_dec and row[i - 1] > row[i]
    return all_dec or all_inc


def is_safe_damp(row):
    for i in range(len(row)):
        if is_safe(row[:i] + row[i + 1 :]):
            return True
    return False


p1 = 0
for row in data:
    p1 += is_safe(row)
print(p1)

p2 = 0
for row in data:
    p2 += is_safe_damp(row)
print(p2)
