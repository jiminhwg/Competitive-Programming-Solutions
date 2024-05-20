A = list(input().split())
A = [int(i) for i in A]
B = int(input())
newlist = []
for a in A:
    a += B
    newlist.append(a)

print(newlist)