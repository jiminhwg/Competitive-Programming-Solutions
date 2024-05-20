import sys
n = int(sys.stdin.readline())
List = []

for a in range(n):
    b,c = map(int, sys.stdin.readline().split())
    List.append(b+c)

for d in List:
    print(d)
