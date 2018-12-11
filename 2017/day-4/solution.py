from string import ascii_lowercase
f = open('input','r')
data = f.readlines()
f.close()
valid = 0
for line in data:
    words = line.strip().split()
    if(len(words) == len(set(words))):
        valid += 1
print('Part A: ', valid)
valid = 0
for line in data:
    words = [''.join(sorted(i)) for i in line.strip().split()]
    if(len(words) == len(set(words))):
        valid += 1
print('Part B: ', valid)
