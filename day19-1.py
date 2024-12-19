from functools import cache
with open('input') as f: lines = [x.strip('\n') for x in f]
towels = lines[0].split(', ')
max_len_t = max(len(t) for t in towels)
t_sets = [{t for t in towels if len(t) == i+1} for i in range(max_len_t)]
patterns = lines[2:]

# Initial attempt to solve the problem: throw a cache at it
# Improved over original attempt by examining each length of towel once

@cache
def part1(p):
    if p == '': return True
    for n in range(max_len_t):
        if p[:n+1] in t_sets[n]:
            if part1(p[n+1:]): return True
    return False

@cache
def part2(p):
    if p == '': return 1
    ways = 0
    for n in range(max_len_t):
        if p[:n+1] in t_sets[n]: ways += part2(p[n+1:])
    return ways

print(sum(part1(p) for p in patterns))
print(sum(part2(p) for p in patterns))
