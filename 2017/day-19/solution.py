from aocd import get_data

raw = get_data(year=2017, day=19)
data = [ line.strip('\n') for line in raw.splitlines() ]
pos = 0+data[0].index('|')*1j
vel = 1j
visited = []
def d(pos):
    return data[int(pos.real)][int(pos.imag)]

def move(pos, vel):
    if d(pos+vel) == ' ':
        if d(pos+1j*vel) != ' ':
            vel *= 1j
        elif d(pos-1j*vel) != ' ':
            vel *= -1j
        else:
            return 0, pos, vel
    pos += vel
    char = d(pos)
    if char.isalpha():
        visited.append(char)
    return 1, pos, vel

running = 1
steps = 0
while running:
    running, pos, vel = move(pos, vel)
    steps += 1
print('Part A: ', ''.join(visited))
print('Part B: ',steps)
