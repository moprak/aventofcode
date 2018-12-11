import numpy as np
import re

data = np.array([ [int(i) for i in re.findall('-?\d+', line)] for line in open('input').readlines() ])

X,Y,A = [],[],[]
for i in range(30000):
    X.append((data[:,0]+i*data[:,2]).max() - (data[:,0]+i*data[:,2]).min())
    Y.append((data[:,1]+i*data[:,3]).max() - (data[:,1]+i*data[:,3]).min())
    A.append(X[i]*Y[i])

t = A.index(min(A))
lx = X[t]+1
ly = Y[t]+1
data[:,:2] += t*data[:,2:]
data[:,0] -= data[:,0].min()
data[:,1] -= data[:,1].min()
canvas = np.zeros((ly,lx),dtype=int)
for j in range(data.shape[0]):
    canvas[data[j,1],data[j,0]] = 1
for j in range(ly):
    print(''.join('@' if p else ' ' for p in canvas[j]))

print('Part B: ', t)
