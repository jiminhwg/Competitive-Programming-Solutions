lst = []
newlst = []
Rows, Column = map(int, input().split())
count = 0

for a in range(Rows):
    b = list(input().split())
    b = [int(i) for i in b]
    lst.append(b)

for c in lst:
    newlst.append(sum(c))

print(sum(newlst))