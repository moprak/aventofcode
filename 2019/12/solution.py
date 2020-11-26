import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist
from aocd import get_data
from functools import reduce
from aocd.models import Puzzle

puzzle = Puzzle(year=2019, day=12)
raw = puzzle.input_data
data = [[int(i) for i in re.findall('-?\d+', line)] for line in raw.splitlines()]

pos = np.array(data)
vel = np.zeros_like(pos)
n, d = pos.shape

def time_step_axis(pos, vel):
    for i in range(len(pos)):
        vel[i] += len(np.where(pos[:] > pos[i])[0]) - len(np.where(pos[:] < pos[i])[0])
    pos[:] += vel[:]

def time_step_3d(pos,vel):
    for j in range(d):
        time_step_axis(pos[:,j],vel[:,j])

def run_sim(pos,vel):
    for _ in range(1000):
        time_step_3d(pos,vel)

run_sim(pos,vel)
puzzle.answer_a = sum( np.abs(pos[i]).sum() * np.abs(vel[i]).sum() for i in range(n))

orig_pos = np.array(data, dtype=int)
pos = orig_pos.copy()
vel = np.zeros_like(pos)
steps = np.zeros(d, dtype=int)
for i in range(d):
    step = 1
    time_step_axis(pos[:,i], vel[:,i])
    while not np.allclose(pos[:,i],orig_pos[:,i]) or not np.allclose(vel[:,i],0):
        step = step + 1
        time_step_axis(pos[:,i], vel[:,i])
    steps[i] = step
puzzle.answer_b = np.lcm.reduce(steps)
