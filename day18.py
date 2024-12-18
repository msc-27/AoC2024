import astar
import grid
with open('input') as f: lines = [x.strip('\n') for x in f]
numbers = [list(map(int, line.split(","))) for line in lines]
corr = {(x,y) for x,y in numbers[:1024]}
grid_size = 70
def trans(p):
    return [((x,y),1) for x,y in grid.atmanhat(p,1) if 0 <= x <= grid_size \
                                                   and 0 <= y <= grid_size \
                                                   and (x,y) not in corr]
def targ(p): return p == (70,70)

a = astar.astar((0,0), trans)
n,path = a.run(targ)
print(n)

for x,y in numbers[1024:]:
    corr.add((x,y))
    if (x,y) in path:
        a = astar.astar((0,0),trans)
        s = a.run(targ)
        if s == None: break
        n,path = s
print(x,y, sep=',')
