import re
with open('input') as f: lines = [x.strip('\n') for x in f]
numbers = [list(map(int, re.findall(r'\d+',line))) for line in lines]
def obtainable(answers, numbers, part):
    # Is any of the answers obtainable from the given numbers?
    if len(numbers) == 1: return numbers[0] in answers
    last = numbers[-1]
    new_answers = []
    for a in answers:
        if a >= last:
            new_answers.append(a - last)
            if last and a % last == 0: new_answers.append(a // last)
            if part == 2 and a > last:
                a_s = str(a)
                l_s = str(last)
                if a_s[-len(l_s):] == l_s:
                    new_answers.append(int(a_s[:len(a_s) - len(l_s)]))
    if new_answers:
        return obtainable(new_answers, numbers[:-1], part)
    else:
        return False
for part in [1,2]:
    print(sum(n[0] for n in numbers if obtainable([n[0]], n[1:], part)))
