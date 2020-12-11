from aocd.models import Puzzle
from collections import defaultdict

puzzle = Puzzle(year=2020, day=10)
raw = puzzle.input_data
data = [ int(i) for i in raw.splitlines() ]

ordered = [0] + sorted(data)
ordered.append(ordered[-1]+3)

t,o =0,0
for i in range(len(ordered)-1):
    if ordered[i+1] - ordered[i] == 3:
        t += 1
    elif ordered[i+1] - ordered[i] == 1:
        o += 1
print(t*o)

options = defaultdict(int)
options[0] = 1
for i in ordered[1:]:
    options[i] = sum([options[i-d] for d in [1,2,3]])
print(options[ordered[-1]])
