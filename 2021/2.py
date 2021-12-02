from aocd.models import Puzzle
from utils import *

puzzle = Puzzle(year=2021, day=2)
raw = puzzle.input_data
data = raw.splitlines()
data = [ alphanum(i) for i in raw.splitlines() ]

x = 0
y = 0
aim = 0
for d, v in data:
  v = int(v)
  if d == 'forward':
    x += v
    y += aim*v
  if d == 'down':
    aim += v
  if d == 'up':
    aim -= v

print('Part 1:', x*aim)
print('Part 2:', x*y)
