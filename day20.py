from collections import defaultdict
import grid
with open('input') as f: lines = [x.strip('\n') for x in f]
def manhat(p,q): return abs(p[0]-q[0]) + abs(p[1]-q[1])
def findin(d,x): return {v for v in d if d[v] == x}

Map = {(x,y):c for y,line in enumerate(lines) for x,c in enumerate(line)}
p = findin(Map,'S').pop()
end = findin(Map,'E').pop()

distance = dict()
prev = None
n = 0
while p != end:
    distance[p] = n
    n += 1
    for q in grid.atmanhat(p,1):
        if Map[q] != '#' and q != prev:
            prev = p
            p = q
            break
distance[p] = n

part1 = 0
part2 = 0
for p in distance:
    for q in grid.inmanhat(p,20):
        if q in distance:
            p_to_q = manhat(p,q)
            if distance[q] - distance[p] - p_to_q >= 100:
                part2 += 1
                if p_to_q == 2: part1 += 1
print(part1)
print(part2)
