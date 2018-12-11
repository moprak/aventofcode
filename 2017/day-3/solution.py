from collections import defaultdict
import numpy as np
pos = 277678
def get_dist(pos):
    nearest_square = int(np.sqrt(pos))
    if( nearest_square%2 == 0 ): nearest_square -= 1
    if( nearest_square **2 == pos ): return (nearest_square-1)
    dist = (nearest_square + 1)/2
    diff = pos - nearest_square ** 2
    dist += abs(diff%(nearest_square+1) - dist)
    return( dist )
print('Part A: ', get_dist(pos))
i = 0
j = 0
grid = defaultdict(int)
grid[(i,j)] = 1
i = 1
grid[(i,j)] = 1
while(pos >= grid[(i,j)]):
    if( i > 0 and j < i and grid[(i,j+1)] == 0):
        j += 1
    elif( j > 0 and i > -j):
        i -= 1
    elif( i < 0 and j > i):
        j -= 1
    elif( i <= -j):
        i += 1
    grid[(i,j)] += sum( grid[(i+1,l)] for l in [j-1,j,j+1] )
    grid[(i,j)] += sum( grid[(i-1,l)] for l in [j-1,j,j+1] )
    grid[(i,j)] += sum( grid[(i,l)] for l in [j-1,j+1] )
print('Part B: ', grid[(i,j)])

