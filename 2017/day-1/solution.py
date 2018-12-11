f = open('input')
data = [int(i) for i in f.read().strip()]
f.close()
tot = data[0] if data[0] == data[-1] else 0
for i in range(len(data) - 2) :
    if( data[i] == data[i+1] ):
        tot += data[i]
print('Part A: ', tot)
s = 0
for i in range(int(len(data)/2)):
    if data[i] == data[ int(len(data)/2) + i]: s += 2*data[i]
print('Part B: ', s)
