import numpy as np
import re
from collections import Counter,defaultdict
import itertools
from string import ascii_uppercase
from copy import deepcopy

f = open('input','r')
data = f.read().strip().splitlines()
f.close()
orig_tree = defaultdict(set)
jobs = set()
for line in data:
    dep  = line.split()[1]
    step  = line.split()[7]
    jobs.add(dep)
    jobs.add(step)
    orig_tree[step].add(dep)
jobs = sorted(jobs)

deptree = deepcopy(orig_tree)
done = []
while(len(done) < len(jobs)):
    for L in jobs:
        for i in done:
            if i in deptree[L]:
                deptree[L].remove(i)
        if(len(deptree[L]) == 0 and (L not in done)):
            done.append(L)
            break
print('Part A: ', ''.join(done))

deptree = deepcopy(orig_tree)
done = []
timer = 0
workers = {}
done_changed = False
while(len(done) < len(jobs)):
    for L in jobs:
        for i in done:
            if i in deptree[L]:
                deptree[L].remove(i)
        if(len(deptree[L]) == 0 and (L not in done) and (len(workers.keys()) < 5) and (L not in workers.keys())) :
            workers[L] = timer
    keys = set(workers.keys())
    for l in keys:
        if(timer == workers[l] + 60 + ascii_uppercase.index(l) + 1):
            workers.pop(l)
            done.append(l)
            done_changed = True
    if(done_changed):
        done_changed = False
        continue
    timer += 1
print('Part B: ', timer)
