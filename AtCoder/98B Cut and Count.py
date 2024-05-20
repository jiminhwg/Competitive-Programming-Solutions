N = int(input())
S = input()

a = 0
b = len(S)

for i in range(b):
    X = set(S[:i + 1])
    Y = set(S[i + 1:b])
    a = max(a, len(X & Y))

print(a)