import numpy as np
import re
from aocd import get_data

raw = get_data(day=20,year=2017)
data = np.array([[int(i) for i in re.findall('-?\d+', line)] for line in raw.splitlines()])
new = np.zeros_like(data[:,:3])
T = 1e5
new[:,:3] = data[:,:3] + T*data[:,3:6] + 0.5 * T*(T+1) * data[:,6:]

res = np.argmin(np.sum(np.abs(new), axis=1))
print('Part A: ', res)

destroyed = []
for T in range(int(50)):
    new[:,:3] = data[:,:3] + T*data[:,3:6] + 0.5 * T* (T+1) * data[:,6:]
    for i in range(1000):
        if i in destroyed: continue
        is_dest = 0
        for j in range(i+1,1000):
            if j not in destroyed:
                if all(new[i,:] == new[j,:]):
                    destroyed.append(j)
                    is_dest = 1
        if( is_dest ): destroyed.append(i)
print('Part B: ', 1000 - len(destroyed) )
