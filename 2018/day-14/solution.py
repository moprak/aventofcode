from blist import blist
from aocd import get_data

raw = get_data()
raw_s = [int(i) for i in raw]
data = blist([3, 7])
orig_l = int(raw)
p0,p1 = 0,1
for c in range(int(1e8)):
    new = [int(i) for i in str(data[p0]+data[p1])]
    data.extend(new)
    p0 = (p0+data[p0]+1)%len(data)
    p1 = (p1+data[p1]+1)%len(data)
    if( raw_s == data[-len(raw):]):
        print('Part B: ', len(data) - len(raw))
        break
    elif (raw_s == data[-len(raw) -1:-1]):
        print('Part B: ', len(data) -1 - len(raw))
        break
    if(c%1000000 == 0): print('.')
print('Part A: ', ''.join(str(i) for i in data[orig_l:orig_l+10]))
