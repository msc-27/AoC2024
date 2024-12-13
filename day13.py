import re
with open('input') as f:
    paras = [p.split('\n') for p in f.read().strip('\n').split('\n\n')]
def solve(para, offset = 0):
    cost = 0
    ax, ay = list(map(int, re.findall('[0-9]+', para[0])))
    bx, by = list(map(int, re.findall('[0-9]+', para[1])))
    px, py = list(map(int, re.findall('[0-9]+', para[2])))
# ax.A + bx.B = px + offset
# ay.A + by.B = py + offset
# Solve the above for A and B. If the solutions are integers, we can win!
# There is exactly one solution unless both buttons move the claw in the
# same overall direction. Assume this doesn't happen.
occur below.
    tx = px + offset
    ty = py + offset
    A_top = tx * by - ty * bx
    A_btm = ax * by - ay * bx
    if A_top % A_btm == 0:
        A = A_top // A_btm
        B_top = tx - ax * A
        if B_top % bx == 0:
            B = B_top // bx
            cost = 3*A + B
    return cost

print(sum(solve(p) for p in paras))
print(sum(solve(p, 10000000000000) for p in paras))
