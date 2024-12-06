import re
data = open('input').read()
insts = list(re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", data))
part1 = 0
part2 = 0
enabled = True
for inst in insts:
    if inst == 'do()':
        enabled = True
    elif inst == "don't()":
        enabled = False
    else:
        n1,n2 = map(int, re.findall('[0-9]+', inst))
        part1 += n1 * n2
        if enabled: part2 += n1 * n2
print(part1)
print(part2)
