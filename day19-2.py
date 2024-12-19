from functools import cache
with open('input') as f: lines = [x.strip('\n') for x in f]
towels = lines[0].split(', ')
max_len_t = max(len(t) for t in towels)
t_sets = [{t for t in towels if len(t) == i+1} for i in range(max_len_t)]
patterns = lines[2:]

# Alternative iterative approach

def solve(p):
    ways = [1] # ways[i] = number of ways to make first i stripes of p
    for i in range(1, len(p)+1):
        ways.append(0)
        for n in range(min(max_len_t, i)):
            if p[i-n-1:i] in t_sets[n]: ways[i] += ways[i-n-1]
    return ways[-1]

solutions = [solve(p) for p in patterns]
print(sum(s > 0 for s in solutions))
print(sum(solutions))
