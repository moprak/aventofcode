from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=5)
raw = puzzle.input_data
data = raw.splitlines()

part_a = 0
grid = set()
for line in data:
    s = line.replace('F','0').replace('B','1').replace('R','1').replace('L','0')
    sid = int(s,2)
    part_a = max(part_a, sid)
    grid.add(sid)

for i in range(128*8):
    if i not in grid and i+1 in grid and i-1 in grid:
        part_b = i
        break

puzzle.answer_a = part_a
puzzle.answer_b = part_b
