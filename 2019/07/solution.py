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

puzzle = Puzzle(year=2019, day=7)
raw = puzzle.input_data
data = [int(i) for i in raw.strip('\n').split(sep=',')]

max_out = 0
for phases in itertools.permutations(range(5)):
    prev_out = 0
    programs = [ intcode.Intcode(data,[phase]) for phase in phases ]
    for program in programs:
        program.add_input(prev_out)
        program.run()
        prev_out = program.outputs.pop()
    max_out = max(max_out, prev_out)
puzzle.answer_a = max_out

max_out = 0
for phases in itertools.permutations(range(5,10)):
    prev_out = 0
    programs = [ intcode.Intcode(data,[phase]) for phase in phases ]
    while all( not program.halted for program in programs):
        for program in programs:
            program.add_input(prev_out)
            program.run()
            if( not program.halted ):
                prev_out = program.outputs.pop()
                program.produced_output = False
    max_out = max(max_out, prev_out)
puzzle.answer_b = max_out
