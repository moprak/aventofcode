from collections import Counter,defaultdict
from aocd.models import Puzzle
import numpy as np
from utils import *

puzzle = Puzzle(year=2021, day=7)
raw = puzzle.input_data
data = ints(raw)
# count = Counter(data)
# score = defaultdict(int)
# score2 = defaultdict(int)
# for pos in range(min(count.keys()),max(count.keys())):
#   for cp in Counter(data):
#     dist = abs(cp-pos)
#     score[pos] += dist*count[cp]
#     score2[pos] += dist*(dist+1)*count[cp]//2
# print(min(score.values()))
# print(min(score2.values()))

a = np.array(sorted(data),dtype=int)
p1 = 1e100
p2 = 1e100
for pos in range(a.min(),a.max()):
  dist = np.abs(a - pos)
  p1 = min(p1, dist.sum())
  p2 = min( p2, (dist*(dist+1)//2).sum())
print(p1)
print(p2)
