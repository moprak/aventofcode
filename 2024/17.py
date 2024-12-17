from aocd.models import Puzzle
from utils import ints


puzzle = Puzzle(year=2024, day=17)
raw = puzzle.input_data
data = ints(raw)
inputs, program = data[:3], data[3:]
def run_prog(inputs, program):
    A, B, C = inputs
    out = []
    ip = 0
    while ip < len(program) -1:
        ins, op = program[ip], program[ip+1]
        combo = [0,1,2,3,A,B,C][op]
        match ins:
           case 0: A = A >> combo
           case 1: B = B^op
           case 2: B = combo %8
           case 4: B = B^C
           case 5: out.append(B%8)
           case 6: B = A >> combo
           case 7: C = A >> combo
           case 3:
               if(A): ip = op -2
        ip += 2
    print(','.join(str(i) for i in out))

run_prog(inputs, program)
def find_A( idx, start):
    if idx < 0:
        print(start)
        return True
    for bits in range(8):
        A = start*8  + bits
        out = ((A%8)^(A>>((A%8)^1))^7)%8
        if out == program[idx] and find_A(idx-1, A):
            return True
    return False
find_A(len(program) - 1, 0)
