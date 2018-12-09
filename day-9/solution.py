import numpy as np
import re
from collections import Counter,defaultdict, deque
import itertools
from string import ascii_uppercase
from copy import deepcopy
from blist import blist

n, l = [ int(i) for i in re.findall('\d+', open('input').read().strip()) ]

def turn_deque(state,value):
    if( value % 23 == 0 ):
        state.rotate(7)
        v = state.pop()
        state.rotate(-1)
        return state, value+v
    else:
        state.rotate(-1)
        state.append(value)
        return state, 0

def play_game_deque(n_players, last_value):
    state = deque([0])
    value = 0
    player = -1
    scores = defaultdict(int)
    while( value < last_value ):
        value += 1
        player = (player+1)%n_players
        state, score = turn_deque(state, value)
        scores[player] += score
    print(max(scores.values()))

def play_game_blist(n_players, last_play):
    seq = blist([0, 2, 1, 3])
    last = 3
    pos = 3
    player = 2
    scores = defaultdict(int)
    for i in range(last, last_play+1):
        player = (player+1) % n_players
        last += 1
        if( last%23 != 0 ):
            pos = (pos+2)%len(seq)
            seq.insert(pos, last)
        else:
            scores[player] += last
            pos = (pos - 7)%len(seq)
            scores[player] += seq.pop(pos)
    print(max(scores.values()))

play_game = play_game_blist
play_game(n,l)
play_game(n,l*100)
