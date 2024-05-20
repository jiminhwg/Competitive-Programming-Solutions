lst = list(input().split())
lst = [int(i) for i in lst]
count = 1

for a in lst:
    count *= a
print(count)