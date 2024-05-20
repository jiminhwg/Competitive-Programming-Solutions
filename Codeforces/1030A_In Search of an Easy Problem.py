n = int(input())
b = list(input().split())

count = 0
for a in b:
    if a == "1":
        count=+1
    else:
        continue

if count==0:
    print("EASY")
else:
    print("HARD")