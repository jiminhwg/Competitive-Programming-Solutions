Friends = list(input().split())
Friends = [int(x) for x in Friends]

Alice = int(input())

NewList = []

for a in Friends:
    NewList.append(abs(a-Alice))

print(min(NewList))
