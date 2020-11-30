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

puzzle = Puzzle(year=2019, day=17)
raw = puzzle.input_data
data = [int(i) for i in raw.strip('\n').split(sep=',')]

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
            val = grid.get((x+min_x,y+min_y),'@')
            reg[y][x] = val
    for i in range(ny):
        print(''.join(reg[i]))

program = intcode.Intcode(data)
grid = {}
x = y = 0
xmax = 0
ymax = 0
while not program.halted:
    program.run()
    if not program.halted:
        o = program.outputs.pop()
        program.produced_output = False
        if( o == 10 ):
            y += 1
            x = 0
        else:
            grid[(x,y)] = chr(o)
            xmax = max(x,xmax)
            ymax = max(y,ymax)
            x += 1

def get_intersections(grid):
    res = []
    painted = list(grid.keys())
    max_x = max(painted)[0]
    min_x = min(painted)[0]
    nx = max_x - min_x + 1
    max_y = max(painted, key = lambda p : p[1])[1]
    min_y = min(painted, key = lambda p : p[1])[1]
    ny = max_y - min_y + 1

    for y in range(min_y,min_y+ny):
        for x in range(min_x, min_x+nx):
            val = grid.get((x,y),'@')
            if( val == '#' ):
                vn = grid.get((x,y+1),'@')
                vs = grid.get((x,y-1),'@')
                ve = grid.get((x+1,y),'@')
                vw = grid.get((x-1,y),'@')
                if(ve == '#' and vn == '#' and vs == '#' and vw =='#'):
                    res.append((x, y))
    return res

puzzle.answer_a = sum([i*j for i,j in get_intersections(grid)])
