import numpy as np
import re
from collections import Counter,defaultdict
import itertools

f = open('input','r')
data = f.read().strip().splitlines()
f.close()
data.sort()

timetable = defaultdict(list)
for i in range(len(data)):
    action = data[i].split(']')[1].strip()
    minute = int(data[i].split(']')[0][-2:])
    if( action == 'wakes up' ):
        uptime = minute
        timetable[guard][downtime:uptime] += 1
    elif( action == 'falls asleep' ):
        downtime = minute
    else:
        guard = int(re.findall(r'-?\d+', action)[0])
        if(timetable[guard] == []): timetable[guard] = np.zeros(60)

most_slept = max(timetable.keys(), key = lambda i: np.sum(timetable[i]) )
print( 'Part A: ', most_slept * timetable[most_slept].argmax() )
most_frequent = max(timetable.keys(), key = lambda i: np.max(timetable[i]) )
print( 'Part B: ', most_frequent * timetable[most_frequent].argmax() )
