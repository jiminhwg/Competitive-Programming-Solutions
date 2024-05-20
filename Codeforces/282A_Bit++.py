Number = int(input())
count = 0
for a in range(Number):
    x = input()
    if '++' in x:
        count += 1
    elif "--" in x:
        count -= 1
print(count)