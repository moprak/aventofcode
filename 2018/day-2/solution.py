import difflib
f = open('input','r')
data = f.read().strip().splitlines()
f.close()
twos = 0
threes = 0
for s in data:
    counts = [s.count(l) for l in s]
    twos += (counts.count(2) > 0)
    threes += (counts.count(3) > 0)
print( 'Part 1: ', twos*threes)

def solve_part_2(data):
    for i in range(len(data)):
        for w in data[i+1:]:
            deltas = list(difflib.ndiff(data[i], w))
            plus = [delta.count('+') for delta in deltas]
            if( sum(plus) == 1 ):
                minus = [delta.count('-') for delta in deltas]
                if( abs( plus.index(1) - minus.index(1) ) == 1 ):
                    print( 'Part 2:', data[i][:minus.index(1)]+data[i][minus.index(1)+1:])
                    return()
solve_part_2(data)
