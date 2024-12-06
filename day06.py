from collections import defaultdict
import moves
with open('input') as f: lines = [x.strip('\n') for x in f]
Map = defaultdict(lambda:'X')
for y,line in enumerate(lines):
    for x,c in enumerate(line):
        Map[(x,y)] = c
def findin(d,x): return {v for v in d if d[v] == x}

start = findin(Map, '^').pop()
guard = moves.Turtle(start, moves.Dir.N)
visited = set() # Locations visited by the guard
states = set()  # States (location, direction) the guard has been in
tested = set()  # Locations we've tried to put an obstruction in
part2 = 0       # Count of successful obstructions
def step(g):
    if Map[g.peek()] == '#':
        g.turnR()
    else:
        g.move()
while Map[guard.loc] != 'X':
    next_loc = guard.peek()
    if Map[next_loc] == '.' and next_loc not in tested:
        # If the guard is approaching an empty space we haven't tested yet,
        # put an obstruction there and run another 'ghost' guard until she
        # either leaves the area or repeats a state
        Map[next_loc] = '#'
        tested.add(next_loc)
        ghost = moves.Turtle(guard.loc, guard.facing)
        g_states = states.copy()
        while Map[ghost.loc] != 'X' and (ghost.loc, ghost.facing) not in g_states:
            g_states.add((ghost.loc, ghost.facing))
            step(ghost)
        part2 += Map[ghost.loc] != 'X'
        # Remove the obstruction
        Map[next_loc] = '.'
    visited.add(guard.loc)
    states.add((guard.loc, guard.facing))
    step(guard)
print(len(visited))
print(part2)
