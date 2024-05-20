A = input().split()
B = input()
count = 0

for a in A:
    if B in a:
        count += 1

print(count)