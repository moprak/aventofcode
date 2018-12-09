from collections import defaultdict
import re
class clist:
    def __init__(self, value):
        self.value = value
        self.next = self
        self.prev = self

    def delete(self, element):
        element.next.prev = element.prev
        element.prev.next = element.next
        return element.value

    def add(self, value):
        new = clist(value)
        new.prev = self
        new.next = self.next
        self.next = new
        new.next.prev = new
        return new

    def next_turn(self, value):
        if value % 23 == 0:
            current = self
            for _ in range(7):
                current = current.prev
            removed_val = self.delete(current)
            return current.next, value + removed_val
        else:
            return self.next.add(value), 0

def run_game(num_players, last_play):
    state = clist(0)
    value = 1
    scores = defaultdict(int)
    player = 0
    while state.value != last_play:
        state, score = state.next_turn(value)
        value += 1
        scores[player] += score
        player = (player+1)%num_players
    return max(scores.values())

n, l = [ int(i) for i in re.findall('\d+', open('input').read().strip()) ]
print(run_game(n, l))
print(run_game(n, l * 100))
