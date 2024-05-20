Cost, AvailableMoney, Wants = map(int, input().split())
lst = []
for a in range(1, Wants+1):
    lst.append(Cost*a)
Remaining = sum(lst) - AvailableMoney

if Remaining < 0:
    print(0)
else:
    print(Remaining)
