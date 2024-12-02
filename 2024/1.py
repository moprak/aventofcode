from collections import Counter

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=1)
data = np.loadtxt(puzzle.input_data_path, dtype=int)
p1 = np.abs(np.sort(data[:, 0]) - np.sort(data[:, 1])).sum()
c = Counter(data[:, 1])
p2 = sum(i * c[i] for i in data[:, 0])
print(p1)
print(p2)
