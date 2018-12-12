import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist
from aocd import get_data
from functools import reduce

raw = get_data()
raw = raw.replace('.','0')
raw = raw.replace('#','1')
data = [ line.strip().split() for line in raw.splitlines() ]

offset = 500
init = '0'*offset+data[0][2]+'0'*offset

data = data[2:]

rules = {}
for line in data:
    rules[line[0]] = line[2]

def next_gen(before):
    after = before
    for i in range(2,len(before)-2):
        after = after[:i] + rules.get(before[i-2:i+3],'0') + before[i+1:]
    return after

def detect_convergence(vals):
    offset = vals[-1] - vals[-2]
    for i in range(len(vals) - 1):
        if vals[i+1] - vals[i] != offset:
            return False
    return True

gens = 1000
gen_sums = np.zeros(gens,dtype=int)
after = init
for gen in range(gens):
    after = next_gen(after)
    if(after[-5:] != '00000' or after[:5] != '00000'):
        print('insufficient buffer! rerun with more padding')
        break
    gen_sums[gen] = sum([i-offset if after[i] == '1' else 0 for i in range(len(init))])
    if( gen > 10 and detect_convergence(gen_sums[gen-10:gen+1]) ):
        print('converged under some definition')
        break

print('Part A: ', gen_sums[19])
print('part B: ', gen_sums[gen] + int(50e9 -(gen+1))* (gen_sums[gen] - gen_sums[gen-1]))
