from functools import cmp_to_key
with open('input') as f:
    paras = [p.split('\n') for p in f.read().strip('\n').split('\n\n')]
rules = {tuple(map(int, line.split('|'))) for line in paras[0]}
def compare(a,b): return 1 if (b,a) in rules else -1
solution = [0,0]
for line in paras[1]:
    pages = list(map(int, line.split(',')))
    s_pages = sorted(pages, key=cmp_to_key(compare))
    solution[pages != s_pages] += s_pages[len(pages) // 2]
print(solution[0])
print(solution[1])
