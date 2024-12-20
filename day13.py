import re
with open('input') as f: paras = f.read().split('\n\n')
def solve(para, offset = 0):
    cost = 0
    ax,ay,bx,by,px,py = list(map(int, re.findall('[0-9]+', para)))
# ax.A + bx.B = px + offset
# ay.A + by.B = py + offset
# Solve the above for A and B. If A and B are nonnegative integers, we can win!
# There is exactly one solution unless both buttons move the claw
# in the same overall direction. Assume this never happens.
    tx = px + offset
    ty = py + offset
    A_top = tx * by - ty * bx
    A_btm = ax * by - ay * bx
    if A_top % A_btm == 0 and A_top // A_btm >= 0:
        A = A_top // A_btm
        B_top = tx - ax * A
        if B_top % bx == 0 and B_top // bx >= 0:
            B = B_top // bx
            cost = 3*A + B
    return cost

print(sum(solve(p) for p in paras))
print(sum(solve(p, 10000000000000) for p in paras))
