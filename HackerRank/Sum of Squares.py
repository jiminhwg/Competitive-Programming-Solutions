lst = list(input().split())
lst = [int(i) for i in lst]

newlst = []
for a in lst:
    newlst.append(a**2)
print(sum(newlst))
