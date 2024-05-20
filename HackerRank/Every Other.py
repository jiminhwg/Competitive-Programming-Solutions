lst = list(input().split())
lst = [int(i) for i in lst]
newlst = []
newnewlst = []
for a in range(len(lst)):
    if a % 2 == 0:
        newlst.append(a)
    else:
        continue

for b in newlst:
    newnewlst.append(lst[b])
    
print(newnewlst)    