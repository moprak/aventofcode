from collections import defaultdict

action_map = {
        ('a',0) : (1,  1, 'b'),
        ('a',1) : (0, -1, 'c'),

        ('b',0) : (1, -1, 'a'),
        ('b',1) : (1,  1, 'd'),

        ('c',0) : (0, -1, 'b'),
        ('c',1) : (0, -1, 'e'),

        ('d',0) : (1,  1, 'a'),
        ('d',1) : (0,  1, 'b'),

        ('e',0) : (1, -1, 'f'),
        ('e',1) : (1, -1, 'c'),

        ('f',0) : (1,  1, 'd'),
        ('f',1) : (1,  1, 'a')
        }

steps = 12481997
state = 'a'
tape = defaultdict(int)
pos = 0

for i in range(steps):
    action = action_map[(state,tape[pos])]
    state = action[-1]
    tape[pos] = action[0]
    pos += action[1]
print(sum(tape.values()))
