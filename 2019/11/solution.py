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
import intcode

puzzle = Puzzle(year=2019, day=11)
raw = puzzle.input_data
data = [int(i) for i in raw.strip('\n').split(sep=',')]

def run_painter(init_val = 0):
    grid = defaultdict(int)
    current_pos = (0,0)
    grid[current_pos] = init_val
    current_dir = 0
    directions= [(0,-1),(1,0),(0,1),(-1,0)]
    program = intcode.Intcode(data)
    while not program.halted:
        program.add_input(grid[current_pos])
        program.run()
        if program.outputs:
            color = program.outputs.pop()
            program.produced_output = False
            grid[current_pos] = color
            program.run()
            if program.outputs:
                turn = program.outputs.pop()
                program.produced_output = False
                current_dir = (current_dir + 1)%4 if turn else (current_dir - 1)%4
                current_pos = ((current_pos[0] + directions[current_dir][0]),(current_pos[1] + directions[current_dir][1]))
    return grid

grid = run_painter()
puzzle.answer_a = len(grid)

grid = run_painter(1)
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
        if grid[(x+min_x,y+min_y)] == 1:
            reg[y][x] = '*'
for i in range(ny):
    print(''.join(reg[i]))
puzzle.answer_b = 'EGZCRKGK'
