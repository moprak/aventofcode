from collections import defaultdict, deque

from aocd.models import Puzzle
from utils import *


puzzle = Puzzle(year=2021, day=12)
raw = puzzle.input_data
data = [ words(i) for i in raw.splitlines() ]
edges = defaultdict(list)
for d in data:
  edges[d[0]].append(d[1])
  edges[d[1]].append(d[0])

def recurse(curr, seen, twice = False):
  if curr == 'end':
    return 1
  if curr in seen and curr.islower():
    if curr == 'start':
      return 0
    if not twice:
      twice = True
    else:
      return 0
  return sum([recurse(child, seen|set([curr]), twice) for child in edges[curr]])
print(recurse('start', set(),True))
print(recurse('start', set()))

# twice = False
# state = ['start', set(['start']), twice]
# q = deque([state])
# p2 = 0
# while q:
#   curr, seen, twice  = q.popleft()
#   for child in edges[curr]:
#     if child == 'end':
#       p2 += 1
#     elif child.isupper():
#       q.append([child, seen, twice])
#     else:
#       if child not in seen:
#         q.append([child, seen|set([child]),twice])
#       elif not twice and child != 'start':
#         q.append([child, seen, True])
# print(p2)
