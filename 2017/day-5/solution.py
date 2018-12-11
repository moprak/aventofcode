import numpy as np
data = np.loadtxt('input', dtype=int)
# data = [0,3,0,1,-3]
i = 0
steps = 0
while True:
    new_i = data[i]+i
    if( data[i] >= 3):
        data[i] -= 1
    else:
        data[i] += 1
    # data[i] += 1
    i = new_i
    steps +=1
    if( new_i < 0 or new_i >= len(data)): break
print(steps)
