N = int(input())
sequence = list(map(int, input().split()))

s_copy = sequence.copy()
s_copy.sort()

b = 0
for a in range(N):
    if sequence[a] != s_copy[a]:
        b += 1
if b > 2:
    print("NO")
else:
    print("YES")
