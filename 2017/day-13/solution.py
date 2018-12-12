import re
import itertools
from aocd import get_data

raw = get_data(day=13, year=2017)
lines = [[int(i) for i in re.findall('\d+', line)] for line in raw.splitlines()]
data = {d:r for d,r in lines}

def lookup(r, t):
    offset = t%(2*(r-1))
    return offset if offset < r else 2*(r-1) - offset

def get_score(delay):
    score = 0
    for i in data:
        if(lookup(data[i],delay+i) == 0):
            score += i*data[i]
    return score

def is_caught(delay):
    for i in data:
        if(lookup(data[i],delay+i) == 0):
            return True
    return False
print(get_score(0))
i = 0
while( is_caught(i) ):
    i += 1
print(i)
