from collections import defaultdict
import grid
with open('input') as f: lines = [x.strip('\n') for x in f]
Map = defaultdict(lambda:'.')
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = c

regions = []
plots = set(Map.keys())
while plots:
    region = set()
    plot = plots.pop()
    typ = Map[plot]
    fringe = {plot}
    while fringe:
        region |= fringe
        new_fringe = set()
        for p in fringe:
            for q in grid.atmanhat(p, 1):
                if q not in region and Map[q] == typ: new_fringe.add(q)
        fringe = new_fringe
    regions.append(region)
    plots -= region

def perimeter(r):
    return sum(q not in r for p in r for q in grid.atmanhat(p,1))
def corners(r):
    corners = 0
    for p in r:
        x,y = p
        for dx in [-1,1]:
            for dy in [-1,1]:
                # Test for convex corner
                corners += (x+dx,y) not in r and (x,y+dy) not in r
                # Test for concave corner
                corners += (x+dx,y) in r and (x,y+dy) in r and (x+dx,y+dy) not in r
    return corners

print(sum(len(r) * perimeter(r) for r in regions))
print(sum(len(r) * corners(r) for r in regions))
