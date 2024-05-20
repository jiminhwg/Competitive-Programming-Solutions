A = int(input())
B = int(input())
C = int(input())

if A < B < C or C < B < A:
    print(B)
elif B < A < C or C < A < B:
    print(A)
else:
    print(C)