List = []
for a in range(0,9):
    n = int(input())
    List.append(n)

SortedList = sorted(List)

print(SortedList[-1])
print(List.index(SortedList[-1])+1)
