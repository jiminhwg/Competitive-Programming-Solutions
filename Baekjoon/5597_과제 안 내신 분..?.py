List1 = []
List2 = [i for i in range(1,31)]
for a in range(0,28):
    List1.append(int(input()))

FinalList = set(List2)-set(List1)
print(min(FinalList))
print(max(FinalList))
