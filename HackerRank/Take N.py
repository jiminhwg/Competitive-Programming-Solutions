lst = list(input().split())
lst = [int(i) for i in lst]
number = int(input())
newlst = []

for a in range(number, 0, -1): 
    newlst.append(a) 
newlst.sort()
print(newlst)
