from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=3)
raw = puzzle.input_data
data = raw.splitlines()

def get_trees(x_step, y_step):
    trees = 0
    for y in range(0,len(data),y_step):
        x = int(y/y_step * x_step)
        if( data[y][x%len(data[0])] == '#'):trees += 1
    return trees

part_a = get_trees(3,1)

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
part_b = 1
for xs,ys in slopes:
    part_b *= get_trees(xs,ys)

puzzle.answer_a = part_a
puzzle.answer_b = part_b
