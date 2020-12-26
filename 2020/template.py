import sys
sys.setrecursionlimit(100000)

import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from aocd import get_data
from functools import reduce
import math
# from blist import blist
# import networkx as nx

from aocd.models import Puzzle
from utils import *


puzzle = Puzzle(year=2020, day=)
raw = puzzle.input_data
data = raw.splitlines()
# data = [ alphanum(i) for i in raw.splitlines() ]

# puzzle.answer_a = ans
# puzzle.answer_b = ans
