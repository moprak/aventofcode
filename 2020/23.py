from collections import deque
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=23)
raw = puzzle.input_data
data = [int(i) for i in raw]
cups = deque(data)
for _ in range(100):
    dest = cups[0] - 1
    if(dest == 0): dest = 9
    cups.rotate(-1)
    pickup = []
    for _ in range(3):
        pickup.append(cups.popleft())
    while (dest in pickup):
        dest -= 1
        if dest < 1:
            dest = 9
    di = cups.index(dest)+1
    for i in range(3):
        cups.insert(di+i, pickup[i])
cups.rotate(-cups.index(1))
print('Part 1:', ''.join([str(i) for i in cups][1:]))

N = int(1e6)
steps =  int(1e7)
bigdata = [int(i) for i in raw] + list(range(10,N+1))

class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

table = {}
for i in range(1,N+1):
    table[i] = Node(i)

for i in range(N):
    table[bigdata[i]].next = table[bigdata[(i+1)%N]]

curr = table[bigdata[0]]
for i in range(steps):
    pickup = curr.next
    curr.next = pickup.next.next.next
    dest = curr.v
    while dest in [curr.v, pickup.v, pickup.next.v, pickup.next.next.v]:
        dest -= 1
        if dest < 1:
            dest = N
    di = table[dest]
    pickup.next.next.next = di.next
    di.next = pickup
    curr = curr.next
print('Part 2:', table[1].next.v * table[1].next.next.v)
