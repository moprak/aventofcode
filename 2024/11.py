from collections import defaultdict
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=11)
raw = puzzle.input_data
data = defaultdict(int)
for i in raw.split():
    data[int(i)] += 1


def blink(data, count):
    for _ in range(count):
        newdata = defaultdict(int)
        for s in data:
            if s == 0:
                newdata[1] += data[s]
            elif len(f"{s}") % 2 == 0:
                l = len(f"{s}")
                newdata[int(f"{s}"[: l // 2])] += data[s]
                newdata[int(f"{s}"[l // 2 :])] += data[s]
            else:
                newdata[s * 2024] += data[s]
        data = newdata
    print(sum(data[s] for s in data))


blink(data, 25)
blink(data, 75)
