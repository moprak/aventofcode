import numpy as np
from collections import Counter
import itertools
changes = np.loadtxt('input', dtype=int)
print('Part 1: ', np.sum(changes))
current = 0
check = {0}
for change in itertools.cycle(changes):
    current += change
    if current in check:
        print('Part 2: ', current)
        break
    check.add(current)
