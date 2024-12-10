import numpy as np
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=9)
raw = puzzle.input_data
data = np.array(list(map(int, list(raw))), dtype=int)
final = np.ones(len(data) * 10, dtype=int) * -1
fs = data[::2]
es = data[1::2]
end = 0
for i in range(len(fs)):
    final[end : end + fs[i]] = i
    end += fs[i] + es[i] if i < len(fs) - 1 else fs[i]
final = final[:end]

for i in range(len(final)):
    if i >= end:
        break
    if final[i] == -1:
        final[i] = final[end - 1]
        final[end - 1] = -1
        end -= 1
        while final[end - 1] == -1:
            end -= 1
final = final[final > -1]
print(sum(i * final[i] for i in range(len(final))))

spaces = []
curr = 0
for i, l in enumerate(data):
    spaces.append([i // 2, curr, l])
    curr += l

for f in spaces[::-2]:
    for e in spaces[1::2]:
        if f[2] <= e[2] and f[1] >= e[1]:
            f[1] = e[1]
            e[1] += f[2]
            e[2] -= f[2]
            break
print(sum(f[0] * ((f[2] - 1 + 2 * f[1]) * f[2]) // 2 for f in spaces[::2]))
