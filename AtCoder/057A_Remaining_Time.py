A, B = map(int, input().split())

if A+B < 24:
    print(A+B)
else:
    print(abs((A+B)-24))