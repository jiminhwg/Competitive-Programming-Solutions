A, B, C = list(map(int, input().split()))

if A != B and A != C:
    print(A)
elif B != A and B != C:
    print(B)
else:
    print(C)


