n = int(input())

output = []
for _ in range(n):
    List = list(map(int, input().split()))
    a = List[0]
    List.sort()
    output.append((len(List) - List.index(a))-1)

for _ in output:
    print(_)
    
    
