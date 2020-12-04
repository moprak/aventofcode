from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=2)
raw = puzzle.input_data
data = raw.splitlines()

grid = ['123','456','789']
ans = ''
x,y=1,1
for s in data:
    for c in s:
        if c == 'U':
            y-=1
        if c == 'D':
            y+=1
        if c == 'R':
            x+=1
        if c == 'L':
            x-=1
        x = max(x,0)
        x = min(x,2)
        y = max(y,0)
        y = min(y,2)
    ans += grid[y][x]
print(ans)
puzzle.answer_a = ans

x,y = 0,2
ans = ''
grid = ['  1  ', ' 234 ', '56789', ' ABC ', '  D  ']
for s in data:
    for c in s:
        xx, yy = x,y
        if c == 'U':
            y-=1
        if c == 'D':
            y+=1
        if c == 'R':
            x+=1
        if c == 'L':
            x-=1
        x = max(x,0)
        x = min(x,4)
        y = max(y,0)
        y = min(y,4)
        if grid[y][x] == ' ':
            x,y = xx, yy
    ans += grid[y][x]
print(ans)
puzzle.answer_b = ans
