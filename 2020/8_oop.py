from aocd.models import Puzzle
from bootcode import Bootcode

puzzle = Puzzle(year=2020, day=8)
raw = puzzle.input_data
data = [ (i.split()[0], int(i.split()[1])) for i in raw.splitlines() ]

program = Bootcode(data)

part_a = program.run()

for i in reversed(program.call_stack):
    if( data[i][0] != 'acc' ):
        program.reset(i)
        part_b = program.run()
        if( program.halted ):
            break
