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

puzzle = Puzzle(year=2019, day=13)
raw = puzzle.input_data
data = [int(i) for i in raw.strip('\n').split(sep=',')]

def get_loc(grid,val):
    idx = list(grid.values()).index(val)
    return list(grid.keys())[idx]

def get_delta(x,y):
    if x == y:
        return 0
    if x < y:
        return -1
    if x > y:
        return 1

def run_arcade(program):
    grid = defaultdict(int)
    while not program.halted:
        for i in range(3):
            program.run()
            program.produced_output = False
        if not program.halted:
            x, y, val = program.outputs
            grid[(x,y)] = val
            for i in range(3):
                program.outputs.pop()
        def joystick_input():
            paddle_x, _ = get_loc(grid, 3)
            ball_x, _ = get_loc(grid, 4)
            display_game(grid)
            return get_delta(ball_x, paddle_x)
        program.input_func = joystick_input
    return grid

def display_game(grid):
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
            if grid[(x+min_x,y+min_y)] == 2:
                reg[y][x] = '*'
            elif grid[(x+min_x,y+min_y)] == 1:
                reg[y][x] = '|'
            elif grid[(x+min_x,y+min_y)] == 3:
                reg[y][x] = '_'
            elif grid[(x+min_x,y+min_y)] == 4:
                reg[y][x] = '@'
    for i in range(ny):
        print(''.join(reg[i]))

program = intcode.Intcode(data)
grid = run_arcade(program)
counts = Counter(grid.values())
puzzle.answer_a = counts[2]

program = intcode.Intcode(data)
program.set(0, 2)
grid = run_arcade(program)
puzzle.answer_b = grid[(-1,0)]
