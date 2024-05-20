A = input().split()
B = input()
count = 0
for a in A:
    if a == B:
        count += 1
    else:
        continue
if count > 0:
    print("Found")
else:
    print("Not Found")