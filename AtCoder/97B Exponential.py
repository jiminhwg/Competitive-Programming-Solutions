X = int(input())
a = 0

for b in range(1, int(X**0.5)+1):
    for c in range(1, 11):
        K = b**c
        if K <= X:
            a = max(a, K)
print(a)