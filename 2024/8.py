import itertools
import numpy as np
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=8)
raw = puzzle.input_data
data = raw.splitlines()

G = np.array([list(row) for row in data])
candidates = np.unique(G)
for coverage in [[1], range(G.size)]:
    antinodes = set()
    for c in candidates:
        if c != ".":
            matches = list(zip(*np.where(G == c)))
            pairs = itertools.permutations(matches, 2)
            for m1, m2 in pairs:
                dx, dy = m1[0] - m2[0], m1[1] - m2[1]
                for dist in coverage:
                    if (
                        0 <= m1[0] + dist * dx < G.shape[0]
                        and 0 <= m1[1] + dist * dy < G.shape[1]
                    ):
                        antinodes.add((m1[0] + dist * dx, m1[1] + dist * dy))
    print(len(antinodes))
