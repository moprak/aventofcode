from collections import defaultdict
from aocd.models import Puzzle
from utils import *


puzzle = Puzzle(year=2021, day=6)
raw = puzzle.input_data
data = ints(raw)
fc = defaultdict(int)
for d in data:
  fc[d] += 1

def simulate(fc):
  new_fc = {}
  for i in range(1,9):
    new_fc[i-1] = fc[i]
  new_fc[8] = fc[0]
  new_fc[6] += fc[0]
  return new_fc

for i in range(256):
  if(i == 80):
    print(sum(fc.values()))
  fc = simulate(fc)
print(sum(fc.values()))
