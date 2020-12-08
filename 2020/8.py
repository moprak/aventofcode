from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=8)
raw = puzzle.input_data
data = [ i.split() for i in raw.splitlines() ]

def run_program(data, mod_index = -1):
    has_repeated = False
    seen = []
    idx = 0
    acc = 0
    while not has_repeated and idx < len(data):
        ins = data[idx][0]
        val = int(data[idx][1])
        if(idx in seen):
            has_repeated = True
        else:
            seen.append(idx)
            if idx == mod_index:
                if ins =='jmp':
                    ins = 'nop'
                elif ins == 'nop':
                    ins = 'jmp'
            if(ins == 'acc'):
                acc += val
                idx += 1
            elif ins == 'jmp':
                idx +=val
            elif ins == 'nop':
                idx +=1
    return (acc, has_repeated, seen)

part_a, _, call_stack = run_program(data)

for i in reversed(call_stack):
    if( data[i][0] != 'acc' ):
        part_b, loop, _ = run_program(data, i)
        if( not loop ):
            break
