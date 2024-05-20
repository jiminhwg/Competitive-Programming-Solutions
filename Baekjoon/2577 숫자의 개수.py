A = int(input())
B = int(input())
C = int(input())
Sum = A*B*C
Sum = [int(x) for x in str(Sum)]

B = 0
for b in range(0,10):
    print(Sum.count(B))
    B = B + 1
    