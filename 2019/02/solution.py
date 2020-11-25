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

puzzle = Puzzle(year=2019, day=2)
raw = puzzle.input_data
data = [ int(i) for i in raw.strip('\n').split(sep=',') ]

def run_program(code, noun, verb):
    program = intcode.Intcode(code)
    program.set(1, noun)
    program.set(2, verb)
    program.run()
    return program.get(0)

part_a = run_program(data, 12, 2)
part_b = next(100*noun + verb for noun in range(100) for verb in range(100) if run_program(data, noun, verb) == 19690720)
