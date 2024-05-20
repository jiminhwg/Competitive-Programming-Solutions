A = list(input().split())
A = [int(i) for i in A]
odd = []
for a in A:
    if a%2 != 0:
        odd.append(a)
odd.sort()
print(odd[-1])