import re
from copy import deepcopy
from aocd.models import Puzzle
from utils import *

puzzle = Puzzle(year=2020, day=16)
raw = puzzle.input_data

fields, mine, nearby = raw.split('\n\n')
mine = pints(mine)

valid_ranges = {}
for line in fields.splitlines():
    field = re.match(r'.+:',line)[0]
    nums = pints(line)
    valid_ranges[field] = [(nums[0],nums[1]),(nums[2],nums[3])]

def is_valid(num, field = None):
    if field:
        for lo, hi in valid_ranges[field]:
            if lo <= num <= hi:
                return True
    else:
        for rs in valid_ranges.values():
            for lo, hi in rs:
                if lo <= num <= hi:
                    return True
    return False

valid_tickets = []
ans = 0
for line in nearby.splitlines():
    nums = pints(line)
    valid = True
    for num in nums:
        if(not is_valid(num)):
            ans += num
            valid = False
    if valid: valid_tickets.append(nums)
print(ans)

fields = set(valid_ranges.keys())
field_positions = [deepcopy(fields) for _ in range(20)]

for ticket in valid_tickets:
    for pos, num in enumerate(ticket):
        for field in fields:
            if ( not is_valid(num, field)) and field in field_positions[pos]:
                field_positions[pos].remove(field)

solved = {}
while len(solved) < 20:
    for p1 in range(20):
        if len(field_positions[p1]) == 1 and p1 not in solved :
            f = field_positions[p1].pop()
            solved[p1] = f
            for p2 in range(20):
                field_positions[p2] -= {f}

print(prod([mine[p] if solved[p].startswith('departure') else 1 for p in range(20)]))
