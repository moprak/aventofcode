from collections import deque
from string import ascii_lowercase
from aocd import get_data

raw = get_data(year=2017,day=16)
data = raw.strip().split(',')

seen = []
def dance(state):
    for ins in data:
        if(ins[0] == 's'):
            state.rotate(int(ins[1:]))
        elif(ins[0] == 'x'):
            i,j = list(map(int,ins[1:].split('/')))
            t = state[i]
            state[i] = state[j]
            state[j] = t
        elif(ins[0] == 'p'):
            i,j = list(map(state.index,ins[1:].split('/')))
            t = state[i]
            state[i] = state[j]
            state[j] = t
    txt = ''.join(state)
    return txt

state = deque(ascii_lowercase[:16])
txt = dance(state)
print('Part A: ', txt)

state = deque(ascii_lowercase[:16])
seen.append(''.join(state))
i = 0
while (True):
    txt = dance(state)
    if(txt in seen):
        break
    i += 1
    seen.append(txt)
cycle_len = i - seen.index(txt) + 1
print('Part B: ', seen[seen.index(txt):][int(1e9%cycle_len)])
