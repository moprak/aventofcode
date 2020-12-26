from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=25)
raw = puzzle.input_data
data = [int(i) for i in raw.splitlines()]

def secret(pub):
    i = 1
    while True:
        if pow(7, i, 20201227) == pub:
            return i
        i+=1

p1, p2 = data
print(pow(p1, secret(p2), 20201227))
print(pow(p2, secret(p1), 20201227))
