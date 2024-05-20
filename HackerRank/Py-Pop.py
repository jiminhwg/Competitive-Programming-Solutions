lst = list(input().split())
lst = [int(i) for i in lst]
newlst = []

for a in lst:
    if a == 100000:
        newlst.append(100000)
    elif a == 300000:
        newlst.append(200000)
    elif a == 2000000:
        newlst.append(1700000)
    else:
        newlst.append(1000000)
print(newlst)
