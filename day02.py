with open('input') as f: ssv = [x.strip().split() for x in f]
reports = [list(map(int, r)) for r in ssv]
def monotonic(r):
    return all(x > y for x,y in zip(r, r[1:])) or \
           all(x < y for x,y in zip(r, r[1:]))
def slow(r):
    return all(abs(x-y) <= 3 for x,y in zip(r, r[1:]))
def check(r):
    return monotonic(r) and slow(r)
def reduced(r):
    for i in range(len(r)): yield r[:i] + r[i+1:]
print(sum(check(r) for r in reports))
print(sum(any(check(rr) for rr in reduced(r)) for r in reports))
