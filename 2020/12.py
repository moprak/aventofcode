from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=12)
raw = puzzle.input_data
data = raw.splitlines()

ori = 'E'
dirs = ['N','E','S','W']
x,y = 0,0
for line in data:
    d = line[0]
    mag = int(line[1:])
    if d == 'F':
        d = ori
    elif d == 'L':
        n_turns = mag//90
        ori = dirs[(dirs.index(ori) - n_turns)%4]
        continue
    elif d == 'R':
        n_turns = mag//90
        ori = dirs[(dirs.index(ori) + n_turns)%4]
        continue

    if d == 'N':
        y +=mag
    elif d == 'S':
        y -=mag
    elif d == 'E':
        x +=mag
    elif d == 'W':
        x-=mag
print('part 1:', abs(x) + abs(y))

x,y = 0,0
wx,wy = 10,1
for line in data:
    d = line[0]
    mag = int(line[1:])
    if d == 'F':
        x += wx * mag
        y += wy * mag
    elif d == 'N':
        wy += mag
    elif d == 'S':
        wy -= mag
    elif d == 'E':
        wx += mag
    elif d == 'W':
        wx -= mag
    elif d == 'L':
        n_turns = mag//90
        for _ in range(n_turns):
            wx, wy = -wy, wx
    elif d == 'R':
        n_turns = mag//90
        for _ in range(n_turns):
            wx, wy = wy, -wx
print('part 2:', abs(x) + abs(y))
