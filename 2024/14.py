import numpy as np
from aocd.models import Puzzle
from utils import ints, prod


puzzle = Puzzle(year=2024, day=14)
raw = puzzle.input_data
data = np.array([ ints(i) for i in raw.splitlines() ])
lx, ly = 101, 103

def score(T):
    final = np.zeros((len(data),2), dtype=int)
    for i in range(len(data)):
        final[i,0] = (data[i,0] + T*data[i,2])%lx
        final[i,1] = (data[i,1] + T*data[i,3])%ly

    quarters = np.zeros(4)
    for i,j in final:
        quarters[0] += i < lx//2 and j < ly//2
        quarters[1] += i < lx//2 and j > ly//2
        quarters[2] += i > lx//2 and j < ly//2
        quarters[3] += i > lx//2 and j > ly//2
    return int(prod(quarters))

print(score(100))
print(min(range(10000), key = score))
