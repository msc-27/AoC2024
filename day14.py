import re
with open('input') as f: lines = [x.strip('\n') for x in f]
robots = [list(map(int, re.findall('-?[0-9]+',line))) for line in lines]

for t in range(1,101*103):
    grid = [['.'] * 101 for y in range(103)]
    for r in robots:
        r[0] = (r[0] + r[2]) % 101
        r[1] = (r[1] + r[3]) % 103
        grid[r[1]][r[0]] = 'X'
# Print a grid for inspection if at least ten robots are horizontally adjacent
    if any('X'*10 in ''.join(row) for row in grid):
        for row in grid: print(''.join(row))
        print('The pattern above appears after', t, 'seconds.')
        print()
    if t == 100:
        q = [0]*4
        for px,py,vx,vy in robots:
            if px < 50 and py < 51: q[0] += 1
            if px > 50 and py < 51: q[1] += 1
            if px < 50 and py > 51: q[2] += 1
            if px > 50 and py > 51: q[3] += 1
        part1 = q[0]*q[1]*q[2]*q[3]
print('Safety factor after 100 seconds: ', part1)
