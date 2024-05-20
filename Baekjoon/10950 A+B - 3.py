Number = int(input())
lst = []
for a in range(Number):
    A, B = map(int, input().split())
    lst.append(A+B)
for b in lst:
    print(b)
