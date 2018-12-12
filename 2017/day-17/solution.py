from collections import deque
from aocd import get_data

raw = get_data(year=2017, day=17)
step = int(raw)
state = deque([])
for i in range(2018):
    state.rotate(-step)
    state.append(i)
print('Part A: ', state[0])

i = 0
for t in range(1,int(50e6)):
    i = (i+step)%t + 1
    if( i == 1 ): ans = t
print('Part B: ', ans)
