from collections import defaultdict
from sympy import isprime
from aocd import get_data

raw = get_data(year=2017,day=23)
data = [ line.strip().split() for line in raw.splitlines() ]
reg = defaultdict(int)
def get_val(s, reg):
    if( s.isalpha() ):
        return reg[s]
    return int(s)

pos = 0
snd = 0
reg['a'] = 0
hack = 0
iters = 0
while 0<= pos < len(data):
    ins = data[pos]
    if( ins[0] == 'set' ):
        reg[ins[1]] = get_val(ins[2],reg)
    elif ins[0] == 'sub':
        reg[ins[1]] -= get_val(ins[2],reg)
    elif ins[0] == 'mul':
        reg[ins[1]] *= get_val(ins[2],reg)
        reg['mul'] += 1
    elif ins[0] == 'add':
        reg[ins[1]] += get_val(ins[2],reg)
    elif( ins[0] == 'jnz' and get_val(ins[1],reg) is not 0):
        pos += get_val(ins[2],reg)
        continue
    pos += 1
    iters += 1
print('Part A: ', reg['mul'])

h = 0
bval = int(int(data[0][2])*100+100000)
cval = bval + 17000
for i in range(bval,cval+1,17):
    if( not isprime(i) ):
        h += 1
print('Part B: ', h)
