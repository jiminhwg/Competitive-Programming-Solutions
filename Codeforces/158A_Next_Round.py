Participants, Place = map(int, input().split())
Scores = list(map(int, input().split()))

NewPlace = Scores[Place-1]
count = 0

for a in Scores:
    if a >= NewPlace and a > 0:
        count += 1

print(count)