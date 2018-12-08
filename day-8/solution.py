import numpy as np
import re
from collections import Counter,defaultdict
import itertools
from string import ascii_uppercase
from copy import deepcopy

data = np.loadtxt('input', dtype = int)
# metadata = []
# def traverse(pos):
#     cc, mc = data[pos:pos+2]
#     pos += 2
#     for i in range(cc):
#         pos = traverse(pos)
#     for i in range(mc):
#         metadata.append(data[pos+i])
#     return pos+mc
# traverse(0)
# print('Part A: ', np.sum(metadata))

def get_val(pos):
    nc, nm = data[pos:pos+2]
    cvals = defaultdict(int)
    meta_sum = 0
    pos += 2
    for i in range(nc):
        pos, cvals[i], msum = get_val(pos)
        meta_sum += msum
    metadata = data[pos:pos+nm]
    meta_sum += sum(metadata)
    if( nc == 0 ):
        value = sum(metadata)
    else:
        value = sum(cvals[i-1] for i in metadata)
    return pos+nm, value, meta_sum

_, value, meta_sum = get_val(0)
print('Part A: ', meta_sum)
print('Part B: ', value)
