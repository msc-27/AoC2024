with open('input') as f: ssv = [x.strip().split() for x in f]
list1 = sorted(int(x[0]) for x in ssv)
list2 = sorted(int(x[1]) for x in ssv)
print(sum(abs(a-b) for a,b in zip(list1, list2)))
print(sum(x * list2.count(x) for x in list1))
