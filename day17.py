import re
with open('input') as f: lines = [x.strip('\n') for x in f]
numbers = [list(map(int, re.findall('[0-9]+',line))) for line in lines]

reg = [numbers[i][0] for i in range(3)]
prog = numbers[4]
output = []

def combo(op):
    if op <= 3: return op
    if op == 4: return reg[0]
    if op == 5: return reg[1]
    if op == 6: return reg[2]

def adv(op): reg[0] >>= combo(op)
def bxl(op): reg[1] ^= op
def bst(op): reg[1] = combo(op) & 7
def jnz(op):
    if reg[0] != 0: return op
def bxc(op): reg[1] ^= reg[2]
def out(op): output.append(combo(op) & 7)
def bdv(op): reg[1] = reg[0] >> combo(op)
def cdv(op): reg[2] = reg[0] >> combo(op)

ops = [adv,bxl,bst,jnz,bxc,out,bdv,cdv]

ip = 0
while ip < len(prog) - 1:
    cmd = ops[prog[ip]]
    op = prog[ip+1]
    r = cmd(op)
    if r != None:
        ip = r
    else:
        ip += 2

print(','.join(str(n) for n in output))

# Reverse engineering of specific program:
# 2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0
# bst 4; bxl 2; cdv 5; bxc 5; adv 3; bxl 7; out 5; jnz 0
# This puts the bottom three bits of A in B, then calculates:
# B = B XOR 2
# C = A >> B
# B = B XOR C XOR 7
# and outputs the bottom three bits of B.
# A is shifted right three places and we continue until A is zero.
# So we go backwards through the output, finding the initial value of A 
# three bits at a time by searching for the numerically smallest bit pattern
# that would give the correct result.
A = 0
for n in prog[::-1]:
    A <<= 3
    for i in range(8):
        b = i ^ 2
        c = (A+i) >> b
        b = b ^ c ^ 7
        if b & 7 == n: break
    A += i
print(A)
