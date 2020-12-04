from collections import Counter,defaultdict, deque
from aocd.models import Puzzle

puzzle = Puzzle(year=2016, day=6)
raw = puzzle.input_data
data = [ i for i in raw.splitlines() ]
word_len = len(data[0])
words = [ ''.join([ s[j] for s in data]) for j in range(word_len) ]
C = [ Counter(s).most_common()[0] for s in words ]
part_a = ''.join([ c for c, _ in C])
C = [ Counter(s).most_common()[-1] for s in words ]
part_b = ''.join([ c for c, _ in C])

puzzle.answer_a = part_a
puzzle.answer_b = part_b
