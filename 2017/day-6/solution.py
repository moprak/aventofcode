import itertools
f = open('input')
d = list(map(int,f.read().strip().split()))
seen = []
steps = 0
while True:
    state = ''.join([str(v)+'_' for v in d])
    if(state in seen): break
    seen.append(state)
    m = max(d)
    mi = d.index(m)
    d[mi] = 0
    for i in range(1,m+1):
        d[(mi+i)%len(d)] += 1

    steps += 1
print('Part A: ', steps)
print('Part B: ', steps - seen.index(state))
