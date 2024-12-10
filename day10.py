from collections import defaultdict
import grid
with open('input') as f: lines = [x.strip('\n') for x in f]
Map = defaultdict(lambda:-1)
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = int(c)
def findin(d,x): return {v for v in d if d[v] == x}

def score(loc):
    h = Map[loc]
    if h == 9: return [{loc}, 1]
    part1, part2 = set(), 0
    for p in grid.atmanhat(loc, 1):
        if Map[p] == h+1:
            a,b = score(p)
            part1 |= a
            part2 += b
    return [part1, part2]

heads = findin(Map, 0)
scores = [score(h) for h in heads]
print(sum(len(s[0]) for s in scores))
print(sum(s[1] for s in scores))
