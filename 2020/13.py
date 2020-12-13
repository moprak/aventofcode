import re
from functools import reduce
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=13)
raw = puzzle.input_data
data = raw.splitlines()

curr_time = int(data[0])
buses = map(int,re.findall('\d+', data[1]))

earliest = 0
for bus in buses:
    btime = int(bus * (curr_time//bus + 1))
    if( btime < earliest or not earliest):
        ans = (btime - curr_time)*bus
        earliest = btime
print('Part 1:', ans)

# Pairs should be list of (ai,ni); outputs x such that x is congruent to ai mod ni for all i
def chinese_remainder(pairs):
    res = 0
    _, N = zip(*pairs)
    P = reduce(lambda x,y: x*y, N)
    for a,n in pairs:
        p = P//n
        res+=a*pow(p,-1,n)*p #could also use Fermat's little theorem pow(p,n-2,n)
    return res%P

pairs = []
for a, n in enumerate(data[1].split(',')):
    if n != 'x':
        pairs.append((-a, int(n)))
print('Part 2:', chinese_remainder(pairs))
