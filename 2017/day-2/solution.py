import numpy as np
data = np.loadtxt('input')
print('Part A: ', data.max(axis=1).sum() - data.min(axis=1).sum())
s = 0
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(j+1,data.shape[1]):
            if(data[i,k] % data[i,j] == 0 ):
                s += data[i,k]/data[i,j]
                break
            if(data[i,j] % data[i,k] == 0 ):
                s += data[i,j]/data[i,k]
                break
print('Part B: ', s)
