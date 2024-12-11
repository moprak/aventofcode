from collections import Counter
from aocd.models import Puzzle


puzzle = Puzzle(year=2024, day=11)
raw = puzzle.input_data
data = Counter(map(int,raw.split()))
def blink(data, count):
    for _ in range(count):
        newdata = Counter()
        for s in data:
            l = len(f"{s}")
            if s == 0:
                newdata[1] += data[s]
            elif l%2 == 0:
                newdata[int(f"{s}"[:l//2])] += data[s]
                newdata[int(f"{s}"[l//2:])] += data[s]
            else:
                newdata[s * 2024] += data[s]
        data = newdata
    print(sum(data[s] for s in data))

blink(data, 25)
blink(data, 75)
