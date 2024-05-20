A, B = map(int, input().split())

if A == B:
    print(A+B)
elif A < B:
    print(B + max(B-1, A))
else:
    print(A + max(A-1, B))
   