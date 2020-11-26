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
import math

puzzle = Puzzle(year=2019, day=10)
raw = puzzle.input_data
data = [ line.strip('\n') for line in raw.splitlines() ]

asteroids = []
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            asteroids.append((j,i))

def get_slope(a1, a2):
    dy = (a1[1] - a2[1])
    dx = (a1[0] - a2[0])
    slope = -math.atan2(dx, dy)
    return slope if slope >= 0 else slope + 2*np.pi

max_viz = 0
for a1 in asteroids:
    slopes = set()
    for a2 in asteroids:
        if a1 != a2:
            slopes.add(get_slope(a1,a2))
    if(len(slopes) > max_viz):
        max_viz = len(slopes)
        max_a = a1
        max_slopes = slopes

puzzle.answer_a = max_viz

a_at_slopes = defaultdict(list)
for a in asteroids:
    if a != max_a:
        slope = get_slope(max_a,a)
        a_at_slopes[slope].append(a)

if(max_viz > 200):
    candidates = a_at_slopes[sorted(a_at_slopes.keys())[199]]
    winner = sorted(candidates,key=lambda a:abs(max_a[0]-a[0])+abs(max_a[1]-a[1]))[0]
    puzzle.answer_b = winner[0]*100 + winner[1]
