import numpy as np
cs = np.loadtxt('input', dtype = int, delimiter = ',')
ubound = cs.max(axis=0)
lbound = cs.min(axis=0)
canvas = -np.ones(ubound+1)
canvas_2 = np.zeros(ubound+1)
scores = np.zeros(len(cs))
for i in range(ubound[0]+1):
    for j in range(ubound[1]+1):
        dists = np.abs(cs[:,0] - i) + np.abs(cs[:,1] - j )
        canvas_2[i,j] = dists.sum()
        if (len(np.where(dists == dists.min())[0]) == 1 ):
            minp = np.argmin(dists)
            scores[minp] += 1
            canvas[i,j] = minp

is_in = np.ones(len(cs), dtype = bool)
for i in range(len(cs)):
    if( i in np.concatenate((np.unique(canvas[:,0]), np.unique(canvas[:,-1]), np.unique(canvas[0,:]), np.unique(canvas[-1,:]))) ): is_in[i] = 0

print('Part A : ',scores[np.arange(len(cs))[is_in]].max())
print('Part B : ', np.sum(canvas_2 < 10000 ) )
