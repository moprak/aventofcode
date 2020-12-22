from copy import deepcopy
from aocd.models import Puzzle
from collections import deque
from utils import *

puzzle = Puzzle(year=2020, day=22)
raw = puzzle.input_data
decks = raw.split('\n\n')
p1,p2 = deque(pints(decks[0])[1:]), deque(pints(decks[1])[1:])

def score(p):
    ans = 0
    for i,v in enumerate(p):
        ans += (len(p)-i) * v
    return ans

def play_game_1(p1,p2):
    while p1 and p2:
        a = p1.popleft()
        b = p2.popleft()
        if a > b:
            p1.extend([a,b])
        else:
            p2.extend([b,a])

    if(len(p1)):
        return score(p1)
    return score(p2)

print(play_game_1(deepcopy(p1), deepcopy(p2)))

def play_game(p1,p2):
    seen_states = set()
    while p1 and p2:
        key = (str(p1), str(p2))
        if key in seen_states:
            return 1, p1
        seen_states.add(key)

        a = p1.popleft()
        b = p2.popleft()
        if( len(p1) < a or len(p2) < b ):
            if( a > b ):
                winner = p1
                winner.extend([a,b])
            else:
                winner = p2
                winner.extend([b,a])
        else:
            retval, _ = play_game(deque(list(p1)[:a]),deque(list(p2)[:b]))
            if retval:
                winner = p1
                winner.extend([a,b])
            else:
                winner = p2
                winner.extend([b,a])
    if(len(p1)):
        return 1, p1
    return 0, p2

_, winner = play_game(deepcopy(p1), deepcopy(p2))
print(score(winner))
