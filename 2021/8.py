from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=8)
raw = puzzle.input_data
data = [d.split('|') for d in raw.splitlines()]

p1 = 0
for d in data:
  for s in d[1].strip().split():
    s = len(list(s))
    if s in [2,3,4,7]:
      p1 +=1
print(p1)

def decode(code,value):
  nummap = {}
  for c in code:
    c = set(list(c))
    if(len(c) == 2):
      nummap[1] = c
    elif(len(c) == 3):
      nummap[7] = c
    elif(len(c) == 4):
      nummap[4] = c
    elif(len(c) == 7):
      nummap[8] = c

  for c in code:
    c = set(list(c))
    if(len(c) == 6):
      if(nummap[1] - c):
        nummap[6] = c
      elif(nummap[4] - c):
        nummap[0] = c
      else:
        nummap[9] = c

  for c in code:
    c = set(list(c))
    if(len(c) == 5):
      if(nummap[1] - c):
        if(c - nummap[6]):
          nummap[2] = c
        else:
          nummap[5] = c
      else:
        nummap[3] = c
  valmap = [nummap[i] for i in range(10)]
  ans = ''
  for v in value:
    v = set(list(v))
    ans += str(valmap.index(v))
  return int(ans)

p2 = 0
for d in data:
  p2 += decode(d[0].strip().split(), d[1].strip().split())
print(p2)
