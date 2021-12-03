from copy import deepcopy
from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=3)
raw = puzzle.input_data
data = raw.splitlines()

N = len(data)
n = len(data[0])
gamma = 0
eps = 0
for i in range(n):
  c1 = len([x for x in data if x[i] == '1'])
  if c1 > N - c1:
    gamma += 2**(n-i-1)
  else:
    eps += 2**(n-i-1)
print(gamma*eps)

ox = deepcopy(data)
for i in range(n):
  c1 = len([x for x in ox if x[i] == '1'])
  N = len(ox)
  if c1 >= N - c1:
    ox = [x for x in ox if x[i] == '1']
  else:
    ox = [x for x in ox if x[i] == '0']
  if len(ox) == 1:
    ox = int(ox.pop(), base=2)
    break

co2 = deepcopy(data)
for i in range(n):
  c1 = len([x for x in co2 if x[i] == '1'])
  N = len(co2)
  if c1 >= N - c1:
    co2 = [x for x in co2 if x[i] == '0']
  else:
    co2 = [x for x in co2 if x[i] == '1']
  if len(co2) == 1:
    co2 = int(co2.pop(), base=2)
    break
print(ox*co2)
