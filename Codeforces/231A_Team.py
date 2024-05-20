Problems = int(input())
lst = []
count = 0
lookfor = "1"
for a in range(Problems):
    Numbers = input().split()
    if Numbers.count("1") >= 2:
        count = count + 1

print(count)

