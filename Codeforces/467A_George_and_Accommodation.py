Number = int(input())
count = 0

for a in range(Number):
    Rooms, People = map(int,input().split())
    if Rooms + 1 < People:
        count += 1
print(count)