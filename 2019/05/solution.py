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

puzzle = Puzzle(year=2019, day=5)
raw = puzzle.input_data
data = [int(i) for i in raw.strip('\n').split(sep=',')]

program = intcode.Intcode(data,[1])
program.run()
puzzle.answer_a = program.outputs.pop()

program = intcode.Intcode(data,[5])
program.run()
puzzle.answer_b = program.outputs.pop()
