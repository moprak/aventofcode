from aocd.models import Puzzle
import math

puzzle = Puzzle(year=2016, day=1)
raw = puzzle.input_data
data = raw.split(', ')
x, y = 0,0
curr = 0
delta = {'R' : 1, 'L' : -1}
revisit = False

seen = set((0,0))
for ins in data:
    ins = ins.strip()
    dr = delta[ins[0]]
    mag = int(ins[1:])
    curr = (curr+dr)%4
    for i in range(1,mag+1):
        if curr == 0:
            y+= 1
        elif curr == 1:
            x+= 1
        elif curr == 2:
            y-= 1
        elif curr == 3:
            x-= 1
        if((x,y) in seen and not revisit):
            print('Part B:', abs(x)+abs(y))
            revisit = True
        seen.add((x,y))
print('Part A:', abs(x)+abs(y))
