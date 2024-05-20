n = int(input())
citizens = list(map(int,input().split()))
count = 0

for a in citizens:
    count = count + (max(citizens)-a)

print(count)

