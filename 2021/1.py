from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=1)
raw = puzzle.input_data
data = [int(i) for i in raw.splitlines()]
p1 = 0
p2 = 0
for i in range(len(data)-1):
  if data[i+1] > data[i]:
    p1 +=1
  if i < len(data)-3 and data[i+3] > data[i]:
    p2 +=1
print(p1)
print(p2)
# puzzle.answer_a = p1
# puzzle.answer_b = p2
