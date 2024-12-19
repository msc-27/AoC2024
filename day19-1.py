from functools import cache
with open('input') as f: lines = [x.strip('\n') for x in f]
towels = lines[0].split(', ')
patterns = lines[2:]

# Initial attempt to solve the problem: throw a cache at it

@cache
def part1(p):
    if p in towels: return True
    for t in towels:
        if p[:len(t)] == t:
            if part1(p[len(t):]): return True
    return False

@cache
def part2(p):
    if p == '': return 1
    ways = 0
    for t in towels:
        if p[:len(t)] == t: ways += part2(p[len(t):])
    return ways

print(sum(part1(p) for p in patterns))
print(sum(part2(p) for p in patterns))
