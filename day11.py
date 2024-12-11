from functools import cache
with open('input') as f: data = f.read().strip()
stones = list(map(int, data.split()))

@cache
def expand(n, c):
    s = str(n)
    if c == 1: return 2 if len(s) % 2 == 0 else 1
    if len(s) % 2 == 0:
        return expand(int(s[:len(s)//2]), c-1) \
             + expand(int(s[len(s)//2:]), c-1)
    nn = n*2024 if n else 1
    return expand(nn, c-1)

print(sum(expand(n, 25) for n in stones))
print(sum(expand(n, 75) for n in stones))
