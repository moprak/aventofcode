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

puzzle = Puzzle(year=2019, day=)
raw = puzzle.input_data
data = [ line.strip('\n').split(sep=',') for line in raw.splitlines() ]
