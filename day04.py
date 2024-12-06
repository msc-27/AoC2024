from collections import defaultdict
with open('input') as f: lines = [x.strip('\n') for x in f]
Map = defaultdict(lambda:'.')
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = c
def findin(d,x): return {v for v in d if d[v] == x}

def check_single_xmas(x,y,dx,dy):
    return Map[(x+dx,y+dy)] == 'M' \
       and Map[(x+dx*2,y+dy*2)] == 'A' \
       and Map[(x+dx*3,y+dy*3)] == 'S'

def check_xmas(x,y): # assuming (x,y) is X
    return sum(check_single_xmas(x,y,i,j) for i in [-1,0,1] for j in [-1,0,1])

def test_ms(x,y):
    c = Map[(x,y)]
    return 1 if c == 'M' else 2 if c == 'S' else 0

def check_cross(x,y): # assuming (x,y) is A
    return test_ms(x-1,y-1) + test_ms(x+1,y+1) == 3 \
       and test_ms(x+1,y-1) + test_ms(x-1,y+1) == 3

print(sum(check_xmas(x,y) for x,y in findin(Map, 'X')))
print(sum(check_cross(x,y) for x,y in findin(Map, 'A')))
