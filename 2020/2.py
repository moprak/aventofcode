import re
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=2)
raw = puzzle.input_data

data = [line for line in raw.splitlines()]
words = [re.findall('\w+',s) for s in data]

part_a = 0
part_b = 0
for i in range(len(words)):
    low = int(words[i][0])
    hi = int(words[i][1])
    c = words[i][2]
    p = words[i][3]
    if low <= p.count(c) <= hi:
        part_a +=1
    low -= 1
    hi -= 1
    if (p[low] == c) ^ (p[hi] == c):
        part_b += 1
puzzle.answer_a = part_a
puzzle.answer_b = part_b
