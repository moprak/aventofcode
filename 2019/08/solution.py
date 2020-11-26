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

puzzle = Puzzle(year=2019, day=8)
data = puzzle.input_data
n = 6
m = 25
layers = [ data[n*m*i:n*m*(i+1)] for i in range(len(data)//n//m) ]
zero_count = [ layer.count('0') for layer in layers ]

min_layer = layers[zero_count.index(min(zero_count))]
puzzle.answer_a = min_layer.count('1')*min_layer.count('2')

answer = '2'*(m*n)
for layer in layers:
    for i in range(int(m*n)):
        if answer[i] == '2':
            answer = answer[:i] + layer[i] + answer[i+1:]
for i in range(n):
    print(answer[m*i:m*(i+1)].replace('1','*').replace('0',' '))

puzzle.answer_b = 'CFLUL'
