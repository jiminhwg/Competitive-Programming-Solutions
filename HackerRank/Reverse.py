lst = list(input().split())
newlst = []

for a in lst[::-1]:
    newlst.append(a)

newlst = [int(i) for i in newlst]

print(newlst)