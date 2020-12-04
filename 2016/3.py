from aocd.models import Puzzle
from utils import *

puzzle = Puzzle(year=2016, day=3)
raw = puzzle.input_data
data = [ pints(i) for i in raw.splitlines() ]

ans = 0
for line in data:
    s = sorted(line)
    if(s[0]+s[1] > s[2]): ans +=1
puzzle.answer_a = ans

ans = 0
for i in range(0,len(data),3):
    for j in range(3):
        s = sorted([data[i][j],data[i+1][j],data[i+2][j]])
        if(s[0]+s[1] > s[2]): ans +=1
puzzle.answer_b = ans
