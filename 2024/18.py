from collections import deque
from aocd.models import Puzzle
from utils import ints

puzzle = Puzzle(year=2024, day=18)
raw = puzzle.input_data
data = [complex(*ints(r)) for r in raw.splitlines()]
L = 70
start = 0
end = L + L * 1j


def find_path(t):
    todo = deque([(0, start)])
    seen = set(data[:t])
    while len(todo):
        score, pos = todo.popleft()
        if pos == end:
            return score
        for dx in 1, 1j, -1, -1j:
            new = pos + dx
            if 0 <= new.real <= L and 0 <= new.imag <= L and new not in seen:
                todo.append((score + 1, new))
                seen.add(new)


print(find_path(1024))
lo, hi = 1024, len(data)
while lo < hi - 1:
    mid = (lo + hi) // 2
    if find_path(mid):
        lo = mid
    else:
        hi = mid
print(f"{data[lo].real:.0f},{data[lo].imag:.0f}")
