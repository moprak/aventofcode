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

puzzle = Puzzle(year=2019, day=6)
raw = puzzle.input_data
data = [ line.strip('\n').split(sep=')') for line in raw.splitlines() ]

def build_dag(orbits):
    dag = defaultdict(list)
    for parent, child in orbits:
        dag[parent].append(child)
    return dag

dag = build_dag(data)
seen = set()
def orbit_count(node, depth):
    if(node in seen): return 0
    seen.add(node)
    return depth + sum( orbit_count(child, depth+1) for child in dag[node])
puzzle.answer_a = (orbit_count('COM', 0))


def build_graph(orbits):
    graph = defaultdict(list)
    for parent, child in orbits:
        graph[parent].append(child)
        graph[child].append(parent)
    return graph

graph = build_graph(data)
seen = set()
def calc_transfers(start, end, counter):
    seen.add(start)
    if start == end:
        print(counter)
        puzzle.answer_b = counter - 2
    for child in graph[start]:
        if child in seen: continue
        calc_transfers(child, end, counter+1)
