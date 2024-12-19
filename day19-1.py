from functools import cache
with open('input') as f: lines = [x.strip('\n') for x in f]
towels = lines[0].split(', ')
max_len_t = max(len(t) for t in towels)
t_sets = [{t for t in towels if len(t) == i+1} for i in range(max_len_t)]
patterns = lines[2:]

# Initial attempt to solve the problem: throw a cache at it
# Improved over original attempt by examining each length of towel once
# Also get rid of separate part 1 solution

@cache
def solve(p):
    if p == '': return 1
    ways = 0
    for n in range(max_len_t):
        if p[:n+1] in t_sets[n]: ways += solve(p[n+1:])
    return ways

solutions = [solve(p) for p in patterns]
print(sum(s > 0 for s in solutions))
print(sum(solutions))
