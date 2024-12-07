import itertools
from operator import add, mul

import numpy as np
from aocd.models import Puzzle

import utils

puzzle = Puzzle(year=2024, day=7)
raw = puzzle.input_data
data = [np.array(utils.ints(i)) for i in raw.splitlines()]


def concat(x, y):
    return int(f"{x}{y}")


def find_possibility(row, p2=False):
    op_arr = [mul, add, concat] if p2 else [mul, add]
    for ops in itertools.product(op_arr, repeat=len(row[2:])):
        res = row[1]
        for k, o in enumerate(ops):
            res = o(res, row[k + 2])
        if res == row[0]:
            return True
    return False


for p2 in [False, True]:
    print(sum(row[0] * find_possibility(row, p2) for row in data))
