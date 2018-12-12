from aocd import get_data

raw = get_data()
data = [ line.strip().split() for line in raw.splitlines() ]

offset = 500
init = '.'*offset+data[0][2]+'.'*offset

data = data[2:]

rules = {}
for line in data:
    rules[line[0]] = line[2]

def next_gen(before):
    after = before
    for i in range(2,len(before)-2):
        after = after[:i] + rules.get(before[i-2:i+3],'0') + before[i+1:]
    return after

def detect_convergence(vals):
    offset = vals[-1] - vals[-2]
    for i in range(len(vals) - 10, len(vals) - 1):
        if vals[i+1] - vals[i] != offset:
            return False
    return True

gens = 1000
gen_sums = []
after = init
for gen in range(gens):
    after = next_gen(after)
    if(after[-5:] != '.....' or after[:5] != '.....'):
        print('insufficient buffer! rerun with more padding')
        break
    gen_sums.append(sum([i-offset if after[i] == '#' else 0 for i in range(len(init))]))
    if( gen > 10 and detect_convergence(gen_sums) ):
        print('naive convergence attained ')
        break

print('Part A: ', gen_sums[19])
print('part B: ', gen_sums[gen] + int(50e9 -(gen+1))* (gen_sums[gen] - gen_sums[gen-1]))
