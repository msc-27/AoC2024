import heapq
with open('input') as f: lines = [x.strip('\n') for x in f]
Map = {(x,y):c for y,line in enumerate(lines) for x,c in enumerate(line)}
def findin(d,x): return {v for v in d if d[v] == x}

start_x, start_y = findin(Map, 'S').pop()
end_x, end_y = findin(Map, 'E').pop()

def trans(state, visited):
# Return all states reachable by a worthwhile move from the current state.
# Include a tile multiple times where a turn occurs;
# this is to simplify comparison of paths in both directions for part 2.
# Consider all valid turns but don't travel on tiles already processed.
    x,y,dx,dy = state
    r = []
    q = (x+dx, y+dy) # Test straight ahead
    if q not in visited and Map[q] != '#': r.append((q+(dx,dy), 1))
    q = (x+dy, y-dx) # Test if anti-clockwise turn is worthwhile
    if Map[q] != '#': r.append(((x,y,dy,-dx), 1000))
    q = (x-dy, y+dx) # Test if clockwise turn is worthwhile
    if Map[q] != '#': r.append(((x,y,-dy,dx), 1000))
    return r

def search(initial_state):
# Return all reachable states with their minimum costs
    tiles_visited = set()
    states_visited = dict()
    queue = []
    heapq.heappush(queue, (0, initial_state))
    while queue:
        cost, state = heapq.heappop(queue)
        states_visited[state] = cost
        tiles_visited.add(state[:2])
        next_states = trans(state, tiles_visited)
        for next_state, next_cost in next_states:
            if next_state not in states_visited:
                new_cost = cost + next_cost
                heapq.heappush(queue, (new_cost, next_state))
    return states_visited
        
forward_costs = search((start_x, start_y, 1, 0))
# Simplification: assume that the end is at a cul-de-sac.
# Therefore the end point can only appear once in the search space.
end_state = next(s for s in forward_costs if s[:2] == (end_x, end_y))
min_cost = forward_costs[end_state]

# Turn in the opposite direction from the end state, then search the entire
# space again in reverse.
edx = end_state[2]
edy = end_state[3]
reverse_costs = search((end_x, end_y, -edx, -edy))

# For each state s, let t be the state formed by reversing the direction of
# travel in s. If the forward cost of s and the reverse cost of t add up to
# min_cost, then the tile of s is on a shortest path.
spectator_friendly = set()
for s in forward_costs:
    sx, sy, sdx, sdy = s
    t = (sx, sy, -sdx, -sdy)
    if t in reverse_costs and forward_costs[s] + reverse_costs[t] == min_cost:
        spectator_friendly.add((sx,sy))

print(min_cost)
print(len(spectator_friendly))
