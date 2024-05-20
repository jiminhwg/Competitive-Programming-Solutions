num = int(input())
List = []

for a in range(num):
    b, c, d = map(int, input().split())
    if b < (c-d):
        List.append("advertise")
    elif b == (c-d):
        List.append("does not matter")
    else:
        List.append("do not advertise")
for e in List:
    print(e)