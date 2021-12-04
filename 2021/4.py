import numpy as np
from aocd.models import Puzzle
from utils import *

puzzle = Puzzle(year=2021, day=4)
raw = puzzle.input_data
data = raw.split('\n\n')
numbers = ints(data[0])
boards = [ np.array([ints(l) for l in board.splitlines()]) for board in data[1:]]

def is_bingo(board, ns):
  ns = set(ns)
  bs = set(np.reshape(board,25))
  for i in range(5):
    s1 = set(board[i,:])
    if ns.issuperset(s1):
      return True, sum(bs - ns)
    s2 = set(board[:,i])
    if ns.issuperset(s2):
      return True, sum(bs - ns)
  return False, 0

def find_board(boards, numbers):
  for i in range(len(numbers)):
    for board in boards:
      check, score = is_bingo(np.copy(board), numbers[:i+1])
      if check:
        return score*numbers[i]
  return 0

print(find_board(boards,numbers))

max_i = 0
for board in boards:
  for i in range(len(numbers)):
    check, score = is_bingo(board,numbers[:i+1])
    if check:
      if i > max_i:
        max_i = i
        max_score = score * numbers[i]
      break
print(max_score)
