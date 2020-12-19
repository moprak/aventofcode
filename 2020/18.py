import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=18)
raw = puzzle.input_data
data = raw.splitlines()

class new_math(int):
    def __mul__(self, right):
        return new_math(int(self) + int(right))
    def __add__(self, right):
        return new_math(int(self) + int(right))
    def __sub__(self, right):
        return new_math(int(self) * int(right))

def calculate(expression, swap = False):
    expression = re.sub(r"(\d+)", r"new_math(\1)", expression)
    expression = expression.replace("*", "-")
    if swap:
        expression = expression.replace("+","*")
    return eval(expression)

print("Part 1:", sum(calculate(l) for l in data))
print("Part 2:", sum(calculate(l, True) for l in data))
