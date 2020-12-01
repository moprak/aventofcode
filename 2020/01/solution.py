from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=1)
raw = puzzle.input_data
data = [int(i) for i in raw.splitlines()]

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i]+data[j] == 2020:
            part_a = data[i]*data[j]
            print('Part A: ', part_a)
        for k in range(j+1, len(data)):
            if data[i]+data[j]+data[k] == 2020:
                part_b = data[i]*data[j]*data[k]
                print('Part B:', part_b)

puzzle.answer_a = part_a
puzzle.answer_b = part_b
