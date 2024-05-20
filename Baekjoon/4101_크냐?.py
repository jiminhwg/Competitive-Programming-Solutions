active = True
List = []
while active:
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        if a>b:
            List.append("Yes")
        else:
            List.append("No")
    else:
        active = False

for c in List:
    print(c)
    
