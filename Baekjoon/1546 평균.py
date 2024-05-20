Number = int(input())
lst = list(input().split())
lst = [int(x) for x in lst]
newlst = []

BiggestNumber = max(lst)

for a in lst:
    newlst.append(a/BiggestNumber*100)

newnewlst = sum(newlst)
print(newnewlst/Number)

