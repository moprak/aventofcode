from collections import Counter
from string import ascii_lowercase
from aocd.models import Puzzle
from utils import *

puzzle = Puzzle(year=2016, day=4)
raw = puzzle.input_data
data = [ alphanum(i) for i in raw.splitlines() ]
part_a = 0

for line in data:
    sid = int(line[-2])
    checksum = line[-1]
    password = ''.join(line[:-2])
    counts = Counter(password)
    top_counts = sorted([(-n,c) for c,n in counts.most_common()])[:5]
    actual_checksum = ''.join([c for _,c in top_counts])
    if(checksum == actual_checksum):
        part_a += sid
        real_pass = ''.join([ascii_lowercase[(sid+ascii_lowercase.index(c))%26] for c in password])
        if real_pass.startswith('north'):
            part_b = sid

print(part_a)
print(part_b)

puzzle.answer_a = part_a
puzzle.answer_b = part_b
