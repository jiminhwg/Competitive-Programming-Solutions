List = []
for a in range(0,10):
    n = int(input())
    List.append(n%42)
print(len(set(List)))

