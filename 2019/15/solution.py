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
import intcode
import random
import networkx as nx

puzzle = Puzzle(year=2019, day=15)
raw = puzzle.input_data
data = [int(i) for i in raw.strip('\n').split(sep=',')]

program = intcode.Intcode(data)
grid = {}
progs = {}
x,y = 0,0
progs[(x,y)] = program
grid[(x,y)] = 100
G = nx.Graph()
to_explore = [(x,y)]

reached_o2 = False

def move(x,y,d):
    if d == 3 :
        x = x - 1
    elif d == 4:
        x = x + 1
    elif d == 2:
        y = y + 1
    else:
        y = y - 1
    return x,y

def display_grid(grid):
    painted = list(grid.keys())
    max_x = max(painted)[0]
    min_x = min(painted)[0]
    nx = max_x - min_x + 1
    max_y = max(painted, key = lambda p : p[1])[1]
    min_y = min(painted, key = lambda p : p[1])[1]
    ny = max_y - min_y + 1

    reg = [ [' ']*nx for _ in range(ny)]
    for y in range(ny):
        for x in range(nx):
            val = grid.get((x+min_x,y+min_y),-1)
            if val == 2:
                reg[y][x] = '*'
            elif val == 1:
                reg[y][x] = ' '
            elif val == 0:
                reg[y][x] = '|'
            elif val == 100:
                reg[y][x] = '@'
    for i in range(ny):
        print(''.join(reg[i]))

while to_explore:
    x,y = to_explore.pop()
    for d in [1,2,3,4]:
        xx, yy = move(x,y,d)
        if((xx,yy) not in progs):
            new_prog = intcode.Intcode(progs[(x,y)].program)
            new_prog.add_input(d)
            new_prog.run()
            output = new_prog.outputs.pop()
            progs[(xx,yy)] = new_prog
            grid[(xx,yy)] = output
            if output:
                G.add_edge((x,y),(xx,yy))
                if( output == 2 ):
                    o_loc = (xx,yy)
                to_explore.append((xx,yy))

puzzle.answer_a = nx.dijkstra_path_length(G,(0,0),o_loc)
puzzle.answer_b = nx.eccentricity(G,o_loc)
