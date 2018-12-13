import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase, ascii_lowercase
from copy import deepcopy
from blist import blist
from aocd import get_data
from functools import reduce


raw = get_data()
data = [ line.strip('\n') for line in raw.splitlines() ]

cart_locs = {}
cart_ops = {}
cart_ors = {}
carts = 0

vels = { '^': (-1,0),
         '>': (0,1),
         '<': (0,-1),
         'v': (1,0)}
ors = ['^', '>', 'v', '<']

for i in range(len(data)):
    line = data[i]
    k = -1
    for _ in range(line.count('^')):
        k = line.index('^',k+1)
        cart_locs[carts]=(i,k)
        cart_ors[carts] = '^'
        carts += 1
    k = -1
    for _ in range(line.count('>')):
        k = line.index('>', k+1)
        cart_locs[carts]=(i,k)
        cart_ors[carts] = '>'
        carts += 1
    k = -1
    for _ in range(line.count('v')):
        k = line.index('v', k+1)
        cart_locs[carts]=(i,k)
        cart_ors[carts] = 'v'
        carts += 1
    k = -1
    for _ in range(line.count('<')):
        k = line.index('<', k+1)
        cart_locs[carts]=(i,k)
        cart_ors[carts] = '<'
        carts += 1
    data[i] = line.replace('^','|').replace('v','|').replace('>','-').replace('<','-')

for i in range(carts):
    cart_ops[i] = 'l'

def rotate(config, op):
    if(op == 'l'): return(ors[ors.index(config) - 1], 's')
    if(op == 's'): return (config, 'r')
    if(op == 'r'): return(ors[(ors.index(config) + 1)%4], 'l')

def turn(config, turn):
    if( turn == '\\' ):
        if( config in ['<','>'] ): return rotate(config, 'r')
        return rotate(config, 'l')
    if( turn == '/' ):
        if( config in ['<','>'] ): return rotate(config, 'l')
        return rotate(config, 'r')

def cart_order():
    return sorted(range(carts), key= lambda c: cart_locs[c])

destroyed = []
def move():
    order = cart_order()
    for c in order:
        if( c in destroyed ): continue
        i,j = cart_locs[c]
        ori = cart_ors[c]
        vx, vy = vels[ori]
        new_loc = (i+vx, j+vy)
        for cart in cart_locs:
            if (cart_locs[cart] == new_loc) and (cart not in destroyed):
                destroyed.append(cart)
                destroyed.append(c)
                break
        cart_locs[c] = new_loc
        if( data[new_loc[0]][new_loc[1]] in ['\\', '/'] ):
            ori, _ = turn(ori, data[new_loc[0]][new_loc[1]])
            cart_ors[c] = ori
        if data[new_loc[0]][new_loc[1]] == '+' :
            cart_ors[c], cart_ops[c] = rotate(ori, cart_ops[c])
    return
while( len(destroyed) < len(cart_locs) - 1 ):
    move()
print( 'Part A: ', cart_locs[destroyed[0]])
print( 'Part B: ', cart_locs[(set(cart_locs) - set(destroyed)).pop()])
