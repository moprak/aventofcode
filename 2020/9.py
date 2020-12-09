import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=9)
raw = puzzle.input_data
data = [int(i) for i in raw.splitlines()]

def checksum(array, value):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
                if array[i] + array[j] == value:
                    return True
    return False

for i in range(25,len(data)):
    if( not checksum(data[i-25:i], data[i]) ):
            print(data[i])
            break

to_check = data[i]

## Slow to run, but quick to write/avoid off by 1 errors
# for i in range(len(data)):
#     for j in range(i+2,len(data)):
#         if sum(data[i:j]) == to_check:
#             print(min(data[i:j]) + max(data[i:j]))
#             break

integrals = np.zeros(len(data)+1)
integrals[1:] = np.cumsum(data)
for i in range(len(integrals)):
    for j in range(i+2,len(integrals)):
        interval_sum = integrals[j] - integrals[i]
        if interval_sum == to_check:
            print(min(data[i:j]) + max(data[i:j]))
            break
        elif interval_sum > to_check:
            break
