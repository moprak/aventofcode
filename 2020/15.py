from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=15)
raw = puzzle.input_data
data = [ int(i) for i in raw.split(',') ]

data = [0,8,15,2,12,1,4]
def play_game(data, nturns):
    spoken = [-1]*nturns
    turns = {}
    for i, v in enumerate(data):
        spoken[i] = data[i]
        if i != len(data) - 1:
            turns[v] = i
    i = len(data) - 1
    while i < nturns-1:
        prev = spoken[i]
        pi = turns.get(prev,-1)
        turns[prev] = i
        if pi != -1:
            spoken[i+1] = (i-pi)
        else:
            spoken[i+1] = 0
        i+=1
    print(spoken[-1])

play_game(data,2020)
play_game(data,30000000)
