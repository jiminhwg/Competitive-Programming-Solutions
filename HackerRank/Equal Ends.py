A = list(input().split())
B = list(input().split())

if A[0] == B[-1] or A[-1] == B[0]:
    print("True")
else:
    print("False")