lst = []
newlst = []
Rows, Column = map(int, input().split())
count1 = 0

for a in range(Rows):
    b = list(input().split())
    b = [int(i) for i in b]
    lst.append(b)

for c in lst:
    for e in c:
        count1 += e

print(count1)

