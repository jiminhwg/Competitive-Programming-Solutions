N, X = map(int, input().split())
A = list(input().split())
A = [int (x) for x in A]
lst = []

for a in A:
    if a < X:
        lst.append(a)
    else:
        continue
for b in lst:
    print(b, end = " ")
