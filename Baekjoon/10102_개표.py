num = int(input())
vote = list(input())

countA = 0
countB = 0

for a in vote:
    if a == "A":
        countA += 1
    else:
        countB += 1

if countA > countB:
    print("A")
elif countA < countB:
    print("B")
else:
    print("Tie")