from itertools import combinations
with open('input') as f: lines = [x.strip('\n') for x in f]
Map = {(x,y): c for y,line in enumerate(lines) for x,c in enumerate(line)}
def findin(d,x): return {v for v in d if d[v] == x}

freqs = set(Map.values()) - {'.'}
antinodes = [set(), set()]
def check_antinode(p, part):
    if p in Map:
        antinodes[part].add(p)
        return True
    return False

for f in freqs:
    for a1, a2 in combinations(findin(Map, f), 2):
        x1, y1 = a1
        x2, y2 = a2
        dx = x2 - x1
        dy = y2 - y1
        check_antinode((x1-dx, y1-dy), 0)
        check_antinode((x2+dx, y2+dy), 0)
        i = 0
        while check_antinode((x1-dx*i, y1-dy*i), 1): i += 1
        i = 0
        while check_antinode((x2+dx*i, y2+dy*i), 1): i += 1
for s in antinodes: print(len(s))
