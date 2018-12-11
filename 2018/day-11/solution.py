import numpy as np

gsn = 8199
canvas = np.zeros((300,300))
rack_id = lambda x: x + 10
def pl(x,y):
    temp = (rack_id(x) * y + gsn)*rack_id(x)
    if(temp >= 100):
        return int(str(temp)[-3]) - 5
    else:
        return -5
for i in range(300):
    for j in range(300):
        canvas[i,j] = pl(i+1,j+1)

i,j=0,0
size = 0
result = {}
while size < 300:
    gridsum = np.zeros((300,300))
    i,j=0,0
    while i < 300-size:
        j =0
        while j < 300-size:
            gridsum[i,j] = canvas[i:i+size,j:j+size].sum()
            j+=1
        i+=1
    maxcoord = np.where(gridsum==gridsum.max())
    result[size] = [maxcoord[0][0]+1,maxcoord[1][0]+1, gridsum.max()]
    size += 1
maxsize = max( np.arange(1,300), key = lambda s: result[s][-1] )
print('Part A: ', result[3][0],',',result[3][1])
print('Part B: ', result[maxsize][0], ',', result[maxsize][1], ',', maxsize)
