from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=10)
raw = puzzle.input_data
data = raw.splitlines()
match = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
    }
iscore = {
    ')':3,
    ']':57,
    '}':1197,
    '>':25137
    }
val = {
    '(':1,
    '[':2,
    '{':3,
    '<':4
    }

def check(l):
  lseen = []
  for c in l:
    if c in '([{<':
      lseen.append(c)
    else:
      if len(lseen):
        if lseen.pop() != match[c]:
          return iscore[c], []
  return 0, lseen

def score(l):
  r = 0
  for c in reversed(l):
    r = r*5 + val[c]
  return r

p1 = 0
scores = []
for l in data:
  t, tomatch = check(l)
  if t:
    p1 += t
  else:
    scores.append(score(tomatch))

scores = sorted(scores)
p2 = scores[len(scores)//2]

print(p1)
print(p2)
