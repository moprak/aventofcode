import re
from collections import defaultdict
from aocd.models import Puzzle

puzzle = Puzzle(year=2020, day=7)
raw = puzzle.input_data
data = raw.splitlines()

parents = defaultdict(list)
children = defaultdict(list)

for line in data:
    parent = re.match(r'(\w+ \w+)', line)[0]
    child_data = re.findall(r'(\d+) (\w+ \w+)', line)
    for count, child in child_data:
        parents[child].append(parent)
        children[parent].append((int(count), child))

gold_containers = set()
def find_gold(color):
    for c in parents[color]:
        gold_containers.add(c)
        find_gold(c)

find_gold('shiny gold')
print(len(gold_containers))
puzzle.answer_a = len(gold_containers)

def bag_counts(color):
    res = 0
    for count, child in children[color]:
        res += count * (1 + bag_counts(child))
    return res

print(bag_counts('shiny gold'))
puzzle.answer_b = bag_counts('shiny gold')


## Extras ##

# BFS instead of DFS
from collections import deque
seen = set()
to_check = deque(['shiny gold'])
while to_check:
    child = to_check.pop()
    if child not in seen:
        seen.add(child)
        for parent in parents[child]:
            to_check.appendleft(parent)

print(len(seen) - 1)
