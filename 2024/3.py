import re

from aocd.models import Puzzle

import utils

puzzle = Puzzle(year=2024, day=3)
raw = puzzle.input_data

p1 = 0
pattern = "mul\(\d+,\d+\)"
matches = re.findall(pattern, raw)

for match in matches:
    p1 += utils.prod(utils.ints(match))
print(p1)

pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
matches = re.findall(pattern, raw)
p2 = 0
flag = True
for match in matches:
    if match == "do()":
        flag = True
    elif match == "don't()":
        flag = False
    else:
        if flag:
            p2 += utils.prod(utils.ints(match))
print(p2)
