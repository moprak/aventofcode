from collections import defaultdict, deque
from aocd import get_data

raw = get_data(year=2017, day=18)
data = [ line.strip().split() for line in raw.splitlines() ]
reg = defaultdict(int)
def get_val(s, reg):
    if( s.isalpha() ):
        return reg[s]
    return int(s)

pos = 0
snd = 0
while True:
    ins = data[pos]
    if( ins[0] == 'snd' ):
        snd = get_val(ins[1],reg)
    elif( ins[0] == 'set' ):
        reg[ins[1]] = get_val(ins[2],reg)
    elif ins[0] == 'mod':
        reg[ins[1]] %= get_val(ins[2],reg)
    elif ins[0] == 'mul':
        reg[ins[1]] *= get_val(ins[2],reg)
    elif ins[0] == 'add':
        reg[ins[1]] += get_val(ins[2],reg)
    elif ins[0] == 'rcv':
        if get_val(ins[1], reg) != 0:
            reg[ins[1]] = snd
            print('Part A: ', snd)
            break
    if( ins[0] != 'jgz' ):
        pos += 1
    else:
        if get_val(ins[1],reg) > 0:
            pos = pos + get_val(ins[2],reg)
        else:
            pos = pos + 1

def run_prog(reg, snd, rcv):
    while 0 <= reg['pos'] < len(data):
        ins = data[reg['pos']]
        if(ins[0] == 'snd'):
            reg['count'] += 1
            snd.append(get_val(ins[1],reg))
        elif( ins[0] == 'set' ):
            reg[ins[1]] = get_val(ins[2],reg)
        elif ins[0] == 'mod':
            reg[ins[1]] %= get_val(ins[2],reg)
        elif ins[0] == 'mul':
            reg[ins[1]] *= get_val(ins[2],reg)
        elif ins[0] == 'add':
            reg[ins[1]] += get_val(ins[2],reg)
        elif ins[0] == 'rcv':
            if( len(rcv) ):
                reg[ins[1]] = rcv.popleft()
            else:
                return 1
        elif( ins[0] == 'jgz' and get_val(ins[1],reg) > 0):
            reg['pos'] += get_val(ins[2],reg)
            continue
        reg['pos'] += 1
    return 0

reg0 = defaultdict(int)
reg1 = defaultdict(int)
snd = deque()
rcv = deque()
reg0['p'] = 0
reg0['pid'] = 0
reg1['p'] = 1
reg1['pid'] = 1
while True:
    p0 = run_prog(reg0, snd, rcv)
    p1 = run_prog(reg1, rcv, snd)
    if( p0 == 0 and p1 == 0):
        break
    if( len(snd) == 0 and len(rcv) == 0):
        break
print("Part B: ", reg1['count'])
