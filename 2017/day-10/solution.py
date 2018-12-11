import numpy as np
from functools import reduce

data = np.loadtxt('input', delimiter=',', dtype=int)
state = np.arange(256)
curr = 0
for i in range(len(data)):
    temp = []
    for j in range(data[i]):
        temp.append(state[(curr+j)%256])
    temp.reverse()
    for j in range(data[i]):
        state[(curr+j)%256] = temp[j]
    curr = (curr + i + data[i])%256
print('Part A : ', state[0]*state[1])

data = [ ord(i) for i in open('input').read().strip()]
data.extend([17,31,73,47,23])
state = np.arange(256)
curr = 0
skip = 0
for _ in range(64):
    for i in range(len(data)):
        temp = []
        for j in range(data[i]):
            temp.append(state[(curr+j)%256])
        temp.reverse()
        for j in range(data[i]):
            state[(curr+j)%256] = temp[j]
        curr = (curr + skip + data[i])%256
        skip += 1
print(''.join('%02x'%reduce(lambda x,y: x^y, state[16*i:16+16*i]) for i in range(16)))
