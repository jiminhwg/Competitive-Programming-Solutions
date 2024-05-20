lst = list(input().split())
lst = [int(i) for i in lst]
newlst = []
newnewlst = []
for a in lst:
    if a % 3 == 0 or a%5 == 0:
        newlst.append(a)

for b in newlst:
    c = b ** 2
    newnewlst.append(c)
    
print(sum(newnewlst))
