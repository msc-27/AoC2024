with open('input') as f:
    paras = [p.split('\n') for p in f.read().strip('\n').split('\n\n')]
Map1 = dict()
Map2 = dict()
for y,line in enumerate(paras[0]):
    for x,c in enumerate(line):
        Map1[(x,y)] = c
        if c == '#': cc = '##'
        if c == 'O': cc = '[]'
        if c == '.': cc = '..'
        if c == '@': cc = '@.'
        Map2[(2*x,y)] = cc[0]
        Map2[(2*x+1,y)] = cc[1]
def findin(d,x): return {v for v in d if d[v] == x}

def get_moves():
    for line in paras[1]:
        for c in line:
            if c == '^': yield 0,-1
            if c == '>': yield 1,0
            if c == 'v': yield 0,1
            if c == '<': yield -1,0

def move_part1(Map, p, dx, dy):
    x,y = p
    n = 1
    while Map[(x+dx*n, y+dy*n)] == 'O': n += 1
    if Map[(x+dx*n, y+dy*n)] == '.':
        if n > 1: Map[(x+dx*n, y+dy*n)] = 'O'
        Map[(x+dx, y+dy)] = '@'
        Map[(x,y)] = '.'
        return (x+dx, y+dy)
    else:
        return p

def move_part2(Map, p, dx, dy):
    x,y = p
    if dy == 0: # Horizontal move
        n = 1
        while Map[(x+dx*n, y)] in '[]': n += 1
        if Map[(x+dx*n, y)] == '.':
            for i in range(n, 0, -1):
                Map[(x+dx*i, y)] = Map[(x+dx*(i-1), y)]
            Map[(x,y)] = '.'
            return (x+dx, y+dy)
        else:
            return p
    else: # Vertical move
        front_row = {p}
        moving = {p}
        while not any(Map[(x, y+dy)] == '#' for x,y in front_row) \
          and not all(Map[(x, y+dy)] == '.' for x,y in front_row):
            new_front = set()
            for q in front_row:
                qx, qy = q
                if Map[(qx, qy+dy)] == '[':
                    new_front.add((qx, qy+dy))
                    new_front.add((qx+1, qy+dy))
                elif Map[(qx, qy+dy)] == ']':
                    new_front.add((qx, qy+dy))
                    new_front.add((qx-1, qy+dy))
            front_row = new_front
            moving |= new_front
        if all(Map[(x,y+dy)] == '.' for x,y in front_row):
            cut = {p:Map[p] for p in moving}
            for q in moving: Map[q] = '.'
            for qx, qy in moving: Map[(qx, qy+dy)] = cut[(qx,qy)]
            return (x+dx, y+dy)
        else:
            return p
    
p = findin(Map1, '@').pop()
for dx,dy in get_moves(): p = move_part1(Map1, p, dx, dy)
print(sum(x + 100*y for x,y in findin(Map1, 'O')))

p = findin(Map2, '@').pop()
for dx,dy in get_moves(): p = move_part2(Map2, p, dx, dy)
print(sum(x + 100*y for x,y in findin(Map2, '[')))
