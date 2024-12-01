from collections import Counter

import numpy as np
from aocd.models import Puzzle

from utils import *

puzzle = Puzzle(year=2024, day=1)
raw = puzzle.input_data
data = [ints(i) for i in raw.splitlines()]
data = np.array(data)
p1 = np.abs(np.sort(data[:, 0]) - np.sort(data[:, 1])).sum()
c = Counter(data[:, 1])
p2 = sum(i * c[i] for i in data[:, 0])
print(p1)
print(p2)
